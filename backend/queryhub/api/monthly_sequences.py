import operator
import datetime
from functools import reduce
from django.db.models import Q
from django.db.models import Count
from ..models import QueryHubModel
from datetime import date, timedelta
from .utils import create_uniform_response
from rest_framework.response import Response
from .tasks import text_search, advenced_filter
from rest_framework import generics, exceptions, serializers, status


class MonthlySequencesSerializer(serializers.ModelSerializer):
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
        obj = (
            obj.values("collection_month")
            .annotate(Count("strain", distinct=True))
            .order_by("date__year", "date__month")
        )
        return obj


class MonthlySequencesView(generics.GenericAPIView):
    serializer_class = MonthlySequencesSerializer

    def post(self, request, *args, **kwargs):
        self.serializer = self.get_serializer(data=request.data)
        if self.serializer.is_valid():
            return Response(self.serializer.validated_data)
        return Response(
            create_uniform_response(self.serializer.errors),
            status=status.HTTP_406_NOT_ACCEPTABLE,
        )
