import operator
import datetime
from functools import reduce
from django.db.models import Q
from django_filters import utils
from ..models import QueryHubModel
from collections import OrderedDict
from datetime import date, timedelta
from .utils import create_uniform_response
from django.core.paginator import Paginator
from rest_framework.response import Response
from .tasks import text_search, advenced_filter
from rest_framework import generics, exceptions, serializers, status
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class GetDataSerializer(serializers.Serializer):
    def validate(self, value):
        request = self.context.get("request").data
        date = request.get("date")
        days = request.get("days")
        clade = request.get("clade")
        page = request.get("page", 1)
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

        obj = obj.values(
            "strain",
            "division",
            "date",
            "lineage",
            "nextclade_pango",
            "clade",
        ).order_by("strain")
        paginator = Paginator(obj, 25)
        response = paginator.page(int(page))
        return {"data": response.object_list, "length": paginator.num_pages}


class GetDataView(generics.GenericAPIView):
    serializer_class = GetDataSerializer

    def post(self, request, *args, **kwargs):
        self.serializer = self.get_serializer(data=request.data)
        if self.serializer.is_valid():
            return Response(self.serializer.validated_data)
        return Response(
            create_uniform_response(self.serializer.errors),
            status=status.HTTP_406_NOT_ACCEPTABLE,
        )
