import datetime
from django.db.models import Count
from datetime import date, timedelta
from queryhub.models import QueryHubModel
from ..utils import create_uniform_response
from rest_framework.response import Response
from rest_framework import generics, exceptions, serializers, status


class StateWiseLastThreemonthsSerializer(serializers.Serializer):
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
            .values("collection_month", "division")
            .annotate(Count("strain", distinct=True))
            .order_by("date__month", "-strain__count")
        )
        d = {}
        for item in QuerySet:
            d.setdefault(item["collection_month"], []).append(item)
        list(d.values())
        return d


class StateWiseLastThreemonthsView(generics.GenericAPIView):
    serializer_class = StateWiseLastThreemonthsSerializer

    def post(self, request, *args, **kwargs):
        self.serializer = self.get_serializer(data=request.data)
        if self.serializer.is_valid():
            return Response(self.serializer.validated_data)
        return Response(
            create_uniform_response(self.serializer.errors),
            status=status.HTTP_406_NOT_ACCEPTABLE,
        )
