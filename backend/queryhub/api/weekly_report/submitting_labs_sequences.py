import datetime
from django_filters import utils
from django.utils import timezone
from django.db.models import Count
from collections import OrderedDict
from dateutil.relativedelta import *
from datetime import date, timedelta
from queryhub.models import QueryHubModel
from ..utils import create_uniform_response
from django.db.models.query import QuerySet
from rest_framework.response import Response
from django_filters.constants import EMPTY_VALUES
from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import generics, exceptions, serializers, status


class SubmittingLabSerializer(serializers.ModelSerializer):
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
            "submitting_lab",
        )

    def validate(self, value):
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
            .values("collection_month", "submitting_lab")
            .annotate(Count("strain", distinct=True))
            .order_by("date__year", "date__month", "-strain__count")
        )
        d = {}
        for item in QuerySet:
            d.setdefault(item["collection_month"], []).append(item)
        list(d.values())
        return d


class SubmittingLabView(generics.GenericAPIView):
    serializer_class = SubmittingLabSerializer

    def post(self, request, *args, **kwargs):
        self.serializer = self.get_serializer(data=request.data)
        if self.serializer.is_valid():
            return Response(self.serializer.validated_data)
        return Response(
            create_uniform_response(self.serializer.errors),
            status=status.HTTP_406_NOT_ACCEPTABLE,
        )
