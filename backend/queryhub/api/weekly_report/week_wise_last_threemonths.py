import datetime
from django.db.models import Count
from datetime import date, timedelta
from queryhub.models import QueryHubModel
from rest_framework.response import Response
from ..utils import create_uniform_response, weekly_report_stacked
from rest_framework import generics, exceptions, serializers, status


class WeeklyThreemonthsSerializer(serializers.Serializer):
    def validate(self, value):
        recent_date = QueryHubModel.objects.values("date").latest("date")
        one_month_ago = datetime.datetime(
            recent_date["date"].year, recent_date["date"].month - 3, 1
        )
        month_end = datetime.datetime(
            recent_date["date"].year, recent_date["date"].month, 1
        ) - datetime.timedelta(seconds=1)
        QuerySet = (
            QueryHubModel.objects.filter(
                date__gte=one_month_ago, date__lte=recent_date["date"]
            )
            .values("collection_week", "who_label")
            .annotate(Count("strain", distinct=True))
            .order_by("date__year")
        )
        d = weekly_report_stacked(QuerySet)
        labels = QueryHubModel.objects.values_list("who_label", flat=True).distinct()
        for j in sorted(labels):
            if not any(d["who_label"] == j for d in d["who_label"]):
                ad = {}
                ad["who_label"] = j
                ad["value"] = [0] * len(d["who_label"][0]["value"])
                ad["value1"] = [0.0] * len(d["who_label"][0]["value"])
                d["who_label"].append(ad)
            d["who_label"] = sorted(d["who_label"], key=lambda d: d["who_label"])
        return d


class WeeklyThreemonthsView(generics.GenericAPIView):
    serializer_class = WeeklyThreemonthsSerializer

    def post(self, request, *args, **kwargs):
        self.serializer = self.get_serializer(data=request.data)
        if self.serializer.is_valid():
            return Response(self.serializer.validated_data)
        return Response(
            create_uniform_response(self.serializer.errors),
            status=status.HTTP_406_NOT_ACCEPTABLE,
        )
