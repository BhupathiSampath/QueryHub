import datetime
from django.db.models import Count
from datetime import date, timedelta
from queryhub.models import QueryHubModel
from rest_framework.response import Response
from ..utils import create_uniform_response, weekly_report_stacked
from rest_framework import generics, exceptions, serializers, status


class LastFourMonthsVariantSerializer(serializers.ModelSerializer):
    date = serializers.DateField(required=False)
    lineage = serializers.CharField(required=False)
    division = serializers.CharField(required=False)
    nextclade_pango = serializers.CharField(required=False)
    strain__count = serializers.IntegerField(read_only=True)

    class Meta:
        model = QueryHubModel
        fields = (
            "strain__count",
            "date",
            "strain",
            "division",
            "lineage",
            "nextclade_pango",
        )

    def validate(self, value):
        recent_date = QueryHubModel.objects.values("date").latest("date")
        one_month_ago = datetime.datetime(
            recent_date["date"].year, recent_date["date"].month - 4, 1
        )
        month_end = datetime.datetime(
            recent_date["date"].year, recent_date["date"].month, 1
        ) - datetime.timedelta(seconds=1)
        QuerySet = (
            QueryHubModel.objects.filter(
                date__gte=one_month_ago, date__lte=recent_date["date"]
            )
            .values("collection_month", "who_label")
            .annotate(Count("strain", distinct=True))
            .order_by("date__year", "date__month", "-who_label")
        )
        d = weekly_report_stacked(QuerySet)
        labels = QueryHubModel.objects.values_list("who_label", flat=True).distinct()
        # labels = []
        # for i in QuerySet1:
        #     labels.append(i["who_label"])
        for j in sorted(labels):
            if not any(d["who_label"] == j for d in d["who_label"]):
                ad = {}
                ad["who_label"] = j
                ad["value"] = [0] * len(d["who_label"][0]["value"])
                ad["value1"] = [0.0] * len(d["who_label"][0]["value"])
                d["who_label"].append(ad)
            d["who_label"] = sorted(d["who_label"], key=lambda d: d["who_label"])
        return d


class LastFourMonthsVariantView(generics.GenericAPIView):
    serializer_class = LastFourMonthsVariantSerializer

    def post(self, request, *args, **kwargs):
        self.serializer = self.get_serializer(data=request.data)
        if self.serializer.is_valid():
            return Response(self.serializer.validated_data)
        return Response(
            create_uniform_response(self.serializer.errors),
            status=status.HTTP_406_NOT_ACCEPTABLE,
        )
