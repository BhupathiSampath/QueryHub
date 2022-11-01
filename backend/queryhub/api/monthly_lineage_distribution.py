import datetime
import pandas as pd
from django_filters import utils
from django.db.models import Count
from ..models import QueryHubModel
from collections import OrderedDict
from datetime import date, timedelta
from dateutil.relativedelta import *
from django.db.models.query import QuerySet
from rest_framework.response import Response
from django_filters.constants import EMPTY_VALUES
from django_filters import rest_framework as filters
from .utils import create_uniform_response, stacked_bar
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import generics, exceptions, serializers, status


class MonthlyLineageSerializer(serializers.ModelSerializer):
    date = serializers.DateField(required=False)
    lineage = serializers.CharField(required=False)
    division = serializers.CharField(required=False)
    nextclade_pango = serializers.CharField(required=False)
    aasubstitutions = serializers.CharField(required=False)
    strain__count = serializers.IntegerField(read_only=True)

    class Meta:
        model = QueryHubModel
        fields = (
            "date",
            "strain",
            "lineage",
            "division",
            "who_label",
            "strain__count",
            "aasubstitutions",
            "nextclade_pango",
        )

    def validate(self, value):
        date = value.get("date")
        lineage = value.get("lineage")
        division = value.get("division")
        nextclade_pango = value.get("nextclade_pango")
        aasubstitutions = value.get("aasubstitutions")
        days = self.context.get("request").data.get("days")
        if not days:
            raise exceptions.ValidationError("Days is rquired field")
        day = datetime.date.today() - timedelta(days=int(days))
        obj = QueryHubModel.objects
        if date:
            obj = obj.filter(date=date)
        if lineage:
            obj = obj.filter(lineage__in=lineage.split(","))
        if not lineage:
            obj = obj.filter(
                lineage__in=[
                    "B.1.617.2",
                    "BA.2",
                    "BA.2.10",
                    "BA.2.38",
                    "BA.2.76",
                    "B.1.1.7",
                    "BA.2.75",
                    "B.1.1",
                    "AY.127",
                    "B.1.617.1",
                ]
            )
        if division:
            obj = obj.filter(division__icontains=division)
        if nextclade_pango:
            obj = obj.filter(nextclade_pango__in=nextclade_pango.split(","))
        if aasubstitutions:
            obj = obj.filter(
                reduce(
                    operator.and_,
                    (
                        Q(aasubstitutions__icontains=x)
                        for x in aasubstitutions.split(",")
                    ),
                )
            )
        obj = (
            obj.filter(date__gte=day)
            .values("collection_month", "lineage")
            .annotate(Count("strain", distinct=True))
            .order_by("date__year", "date__month")
        )
        return stacked_bar(obj)


class LineageMonthlyView(generics.GenericAPIView):
    serializer_class = MonthlyLineageSerializer

    def post(self, request, *args, **kwargs):
        self.serializer = self.get_serializer(data=request.data)
        if self.serializer.is_valid():
            return Response(self.serializer.validated_data)
        return Response(
            create_uniform_response(self.serializer.errors),
            status=status.HTTP_406_NOT_ACCEPTABLE,
        )
