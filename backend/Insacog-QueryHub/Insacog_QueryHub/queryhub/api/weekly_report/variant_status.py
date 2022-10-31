import datetime
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


class VariantStatusSerializer(serializers.ModelSerializer):
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
        QuerySet1 = (
            QueryHubModel.objects.filter(
                date__gte="2021-01-01",
            )
            .values_list("collection_month")
            .order_by("date__year", "date__month")
            .distinct()
        )
        months = []
        for i in QuerySet1:
            months.extend(i)
        QuerySet = (
            QueryHubModel.objects.filter(
                date__gte="2021-01-01",
            )
            .values("collection_week", "who_label")
            .annotate(Count("strain", distinct=True))
            .order_by("date__year")
        )
        return weekly_report_stacked(QuerySet)


class VariantStatusView(generics.GenericAPIView):
    serializer_class = VariantStatusSerializer

    def post(self, request, *args, **kwargs):
        self.serializer = self.get_serializer(data=request.data)
        if self.serializer.is_valid():
            return Response(self.serializer.validated_data)
        return Response(
            create_uniform_response(self.serializer.errors),
            status=status.HTTP_406_NOT_ACCEPTABLE,
        )
