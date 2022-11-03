import operator
import datetime
import numpy as np
from functools import reduce
from django.db.models import Q
from django.db.models import Count
from ..models import QueryHubModel
from datetime import date, timedelta
from rest_framework.response import Response
from .tasks import text_search, advenced_filter
from .utils import create_uniform_response, stacked_bar
from rest_framework import generics, exceptions, serializers, status


class StateLineageClassSerializer(serializers.ModelSerializer):
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
            obj.values("division", "who_label")
            .annotate(Count("strain", distinct=True))
            .order_by("-strain__count")
        )
        data = stacked_bar(obj)
        lst = np.zeros((len(data["who_label"][1]["value"]),), dtype=int)
        for i in range(len(data["who_label"])):
            lst += np.array(data["who_label"][i]["value"])
        for i in range(len(data["division"]["division"])):
            data["division"]["division"][i] += f"__{lst[i]}"
        return data


class StateLineageClassification(generics.GenericAPIView):
    serializer_class = StateLineageClassSerializer

    def post(self, request, *args, **kwargs):
        self.serializer = self.get_serializer(data=request.data)
        if self.serializer.is_valid():
            return Response(self.serializer.validated_data)
        return Response(
            create_uniform_response(self.serializer.errors),
            status=status.HTTP_406_NOT_ACCEPTABLE,
        )
