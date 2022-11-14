from django.db.models import Q
from django.db.models import Prefetch
from queryhub.models import QueryHubModel
from rest_framework.response import Response
from queryhub.api.utils import create_uniform_response
from rest_framework import generics, exceptions, serializers, status


class FrontendStatsSerializer(serializers.Serializer):
    def validate(self, value):
        obj = self.context["view"].get_queryset().objects
        total = obj.count()
        state = obj.values_list("division", flat=True).distinct().count()
        lineages = obj.values_list("lineage", flat=True).distinct().count()
        nextcladepango = (
            obj.exclude(clade=None)
            .values_list("nextclade_pango", flat=True)
            .distinct()
            .count()
        )
        clade = (
            obj.exclude(clade=None).values_list("clade", flat=True).distinct().count()
        )
        output = {
            "total": total,
            "clade": clade,
            "state": state,
            "lineages": lineages,
            "nextcladepango": nextcladepango,
        }
        return output


class FrontendStatsView(generics.GenericAPIView):
    queryset = QueryHubModel
    serializer_class = FrontendStatsSerializer

    def post(self, request, *args, **kwargs):
        self.serializer = self.get_serializer(data=request.data)
        if self.serializer.is_valid():
            return Response(self.serializer.validated_data)
        return Response(
            create_uniform_response(self.serializer.errors),
            status=status.HTTP_406_NOT_ACCEPTABLE,
        )
