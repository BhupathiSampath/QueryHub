import datetime
from itertools import groupby
from django_filters import utils
from django.utils import timezone
from django.db.models import Count
from collections import OrderedDict
from dateutil.relativedelta import *
from datetime import date, timedelta
from queryhub.models import QueryHubModel
from django.db.models.query import QuerySet
from rest_framework.response import Response
from django_filters.constants import EMPTY_VALUES
from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView
from ..utils import create_uniform_response, weekly_report_stacked
from rest_framework import generics, exceptions, serializers, status


def key_func(k):
    return k["region_type"]


class RegionwiseAnalysisSerializer(serializers.ModelSerializer):
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
        QuerySet = (
            QueryHubModel.objects.filter(date__gte="2022-01-01")
            .values("region_type", "collection_week", "who_label")
            .annotate(Count("strain", distinct=True))
            .order_by("date__year")
        )
        QuerySet = sorted(QuerySet, key=key_func)
        for key, value in groupby(QuerySet, key_func):
            b.append(list(value))
            for i in b:
                c[key] = i
        for i in c:
            for items in c[i]:
                del items["region_type"]
            d[i] = weekly_report_stacked(c[i])
        QuerySet1 = QueryHubModel.objects.values("who_label").distinct()
        labels = []
        for i in QuerySet1:
            labels.append(i["who_label"])
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


class Regionwisedata2022(generics.GenericAPIView):
    serializer_class = RegionwiseAnalysisSerializer

    def post(self, request, *args, **kwargs):
        self.serializer = self.get_serializer(data=request.data)
        if self.serializer.is_valid():
            return Response(self.serializer.validated_data)
        return Response(
            create_uniform_response(self.serializer.errors),
            status=status.HTTP_406_NOT_ACCEPTABLE,
        )
