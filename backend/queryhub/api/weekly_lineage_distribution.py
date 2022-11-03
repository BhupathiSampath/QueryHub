import operator
import datetime
from functools import reduce
from django.db.models import Q
from django.db.models import Count
from ..models import QueryHubModel
from datetime import date, timedelta
from rest_framework.response import Response
from .utils import create_uniform_response, stacked_bar
from rest_framework import generics, exceptions, serializers, status


class WeeklyLineageSerializer(serializers.ModelSerializer):
    date = serializers.DateField(required=False)
    clade = serializers.CharField(required=False)
    strain = serializers.CharField(required=False)
    lineage = serializers.CharField(required=False)
    division = serializers.CharField(required=False)
    aadeletions = serializers.CharField(required=False)
    nextclade_pango = serializers.CharField(required=False)
    aasubstitutions = serializers.CharField(required=False)

    class Meta:
        model = QueryHubModel
        fields = (
            "date",
            "clade",
            "strain",
            "lineage",
            "division",
            "aadeletions",
            "aasubstitutions",
            "nextclade_pango",
        )

    def validate(self, value):
        date = value.get("date")
        clade = value.get("clade")
        strain = value.get("strain")
        lineage = value.get("lineage")
        division = value.get("division")
        aadeletions = value.get("aadeletions")
        nextclade_pango = value.get("nextclade_pango")
        aasubstitutions = value.get("aasubstitutions")
        params = self.context.get("request").data
        days = params.get("days")
        search = params.get("search")
        present = params.get("present")
        obj = QueryHubModel.objects
        if search:
            obj = obj.filter(
                Q(date__icontains=search_text)
                | Q(lineage__icontains=search_text)
                | Q(division__icontains=search_text)
                | Q(strain__icontains=search_text)
                | Q(nextclade_pango__icontains=search_text)
                | Q(aasubstitutions__icontains=search_text)
                | Q(aadeletions__icontains=search_text)
                | Q(clade__icontains=search_text)
            )
        if days and present == False:
            last_date = QueryHubModel.objects.values("date").latest("date")
            day = last_date["date"] - timedelta(days=int(days))
            obj = obj.filter(date__gte=day)
        if days and present == True:
            day = datetime.date.today() - timedelta(days=int(days))
            obj = obj.filter(date__gte=day)
        if date:
            obj = obj.filter(date=date)
        if clade:
            obj = obj.filter(clade__in=clade.split(","))
        if strain:
            obj = obj.filter(strain__in=strain.split(","))
        if lineage:
            obj = obj.filter(lineage__in=lineage.split(","))
        if division:
            obj = obj.filter(division__in=division.split(","))
        if nextclade_pango:
            obj = obj.filter(nextclade_pango__in=nextclade_pango.split(","))
        if aadeletions:
            obj = obj.filter(
                reduce(
                    operator.and_,
                    (Q(aadeletions__icontains=x) for x in aadeletions.split(",")),
                )
            )
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
        obj = (
            obj.values("collection_week", "lineage")
            .annotate(Count("strain", distinct=True))
            .order_by("date__year", "date__week")
        )
        return stacked_bar(obj)


class LineageWeeklyView(generics.GenericAPIView):
    serializer_class = WeeklyLineageSerializer

    def post(self, request, *args, **kwargs):
        self.serializer = self.get_serializer(data=request.data)
        if self.serializer.is_valid():
            return Response(self.serializer.validated_data)
        return Response(
            create_uniform_response(self.serializer.errors),
            status=status.HTTP_406_NOT_ACCEPTABLE,
        )
