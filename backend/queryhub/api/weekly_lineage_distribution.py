import operator
import datetime
from functools import reduce
from .utils import stacked_bar
from django.db.models import Q
from django.db.models import Count
from ..models import QueryHubModel
from datetime import date, timedelta
from rest_framework.response import Response
from .tasks import text_search, advenced_filter
from rest_framework import generics, exceptions, serializers, status


class WeeklyLineageSerializer(serializers.ModelSerializer):
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
            obj = text_search(search, obj)
        obj = advenced_filter(
            obj,
            days,
            date,
            clade,
            strain,
            lineage,
            present,
            division,
            aadeletions,
            nextclade_pango,
            aasubstitutions,
        )
        if not lineage:
            obj = obj.filter(
                lineage__in=[
                    "BA.2",
                    "B.1.1",
                    "AY.127",
                    "BA.2.10",
                    "BA.2.38",
                    "B.1.1.7",
                    "BA.2.75",
                    "BA.2.76",
                    "B.1.617.2",
                    "B.1.617.1",
                ]
            )
        obj = (
            obj.values("collection_week", "lineage")
            .annotate(Count("strain", distinct=True))
            .order_by("date__year", "collection_week")
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
