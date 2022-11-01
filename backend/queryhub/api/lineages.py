from django.db.models import Count
from ..models import QueryHubModel
from collections import OrderedDict
from .utils import create_uniform_response
from rest_framework.response import Response
from rest_framework import generics, exceptions, serializers, status


class LineageCountSerializer(serializers.ModelSerializer):
    date = serializers.DateField(required=False)
    lineage = serializers.CharField(required=False)
    division = serializers.CharField(required=False)
    aasubstitutions = serializers.CharField(required=False)
    nextclade_pango = serializers.CharField(required=False)

    class Meta:
        model = QueryHubModel
        fields = (
            "date",
            "strain",
            "lineage",
            "division",
            "aasubstitutions",
            "nextclade_pango",
        )

    def validate(self, value):
        date = value.get("date")
        lineage = value.get("lineage")
        division = value.get("division")
        nextclade_pango = value.get("nextclade_pango")
        aasubstitutions = value.get("aasubstitutions")
        obj = QueryHubModel.objects
        if date:
            obj = obj.filter(date=date)
        if lineage:
            obj = obj.filter(lineage__in=lineage.split(","))
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
