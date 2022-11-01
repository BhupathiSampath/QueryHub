import datetime
from itertools import groupby
from django.db.models import Count
from datetime import date, timedelta
from queryhub.models import QueryHubModel
from rest_framework.response import Response
from ..utils import create_uniform_response, weekly_report_stacked
from rest_framework import generics, exceptions, serializers, status


def key_func(k):
    return k["collection_month"]


class VariantStatusStatewiseSerializer(serializers.ModelSerializer):
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
        a = []
        b = []
        c = {}
        d = {}
        recent_date = QueryHubModel.objects.values("date").latest("date")
        one_month_ago = datetime.datetime(
            recent_date["date"].year, recent_date["date"].month - 2, 1
        )
        month_end = datetime.datetime(
            recent_date["date"].year, recent_date["date"].month, 1
        ) - datetime.timedelta(seconds=1)
        QuerySet = (
            QueryHubModel.objects.filter(
                date__gte=one_month_ago, date__lte=recent_date["date"]
            )
            .values("collection_month", "division", "who_label")
            .annotate(Count("strain", distinct=True))
            .order_by("division")
        )
        QuerySet = sorted(QuerySet, key=key_func)
        for key, value in groupby(QuerySet, key_func):
            b.append(list(value))
            for i in b:
                c[key] = i
        for i in c:
            for items in c[i]:
                del items["collection_month"]
            d[i] = weekly_report_stacked(c[i])
        labels = QueryHubModel.objects.values_list("who_label", flat=True).distinct()
        # labels = []
        # for i in QuerySet1:
        #     labels.append(i["who_label"])
        for i in d.values():
            for j in sorted(labels):
                if not any(d["who_label"] == j for d in i["who_label"]):
                    ad = {}
                    ad["who_label"] = j
                    ad["value"] = [0] * len(i["who_label"][0]["value"])
                    ad["value1"] = [0.0] * len(i["who_label"][0]["value"])
                    i["who_label"].append(ad)
            i["who_label"] = sorted(i["who_label"], key=lambda d: d["who_label"])
        return d


class VariantStatusbyStatesView(generics.GenericAPIView):
    serializer_class = VariantStatusStatewiseSerializer

    def post(self, request, *args, **kwargs):
        self.serializer = self.get_serializer(data=request.data)
        if self.serializer.is_valid():
            return Response(self.serializer.validated_data)
        return Response(
            create_uniform_response(self.serializer.errors),
            status=status.HTTP_406_NOT_ACCEPTABLE,
        )
