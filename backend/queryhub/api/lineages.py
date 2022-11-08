import operator
import datetime
from functools import reduce
from django.db.models import Q
from django.db.models import Count
from ..models import QueryHubModel
from collections import OrderedDict
from datetime import date, timedelta
from .utils import create_uniform_response
from rest_framework.response import Response
from .tasks import text_search, advenced_filter
from rest_framework import generics, exceptions, serializers, status


class LineageCountSerializer(serializers.Serializer):
    def validate(self, value):
        request = self.context.get("request").data
        date = request.get("date")
        days = request.get("days")
        clade = request.get("clade")
        search = request.get("search")
        strain = request.get("strain")
        division = request.get("state")
        present = request.get("present")
        lineage = request.get("pangolineage")
        aadeletions = request.get("deletion")
        aasubstitutions = request.get("substitution")
        nextclade_pango = request.get("nextcladelineage")
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
        lineage_count = obj.values("lineage").distinct().count()
        genome_sequence = obj.values("strain").distinct().count()
        lineages_distribution = obj.values("lineage").annotate(
            Count("strain", distinct=True)
        )
        temp = {
            "lineage_count": lineage_count,
            "genome_sequence": genome_sequence,
            "lineages_distribution": lineages_distribution,
        }
        return temp


class UniqeLineageCount(generics.GenericAPIView):
    serializer_class = LineageCountSerializer

    def post(self, request, *args, **kwargs):
        self.serializer = self.get_serializer(data=request.data)
        if self.serializer.is_valid():
            return Response(self.serializer.validated_data)
        return Response(
            create_uniform_response(self.serializer.errors),
            status=status.HTTP_406_NOT_ACCEPTABLE,
        )
