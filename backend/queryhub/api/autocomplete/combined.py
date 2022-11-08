from django.db.models import Q
from django.db.models import Prefetch
from queryhub.models import QueryHubModel
from rest_framework.response import Response
from queryhub.api.utils import create_uniform_response
from rest_framework import generics, exceptions, serializers, status


class CombinedAutoCompleteSerializer(serializers.Serializer):
    def validate(self, value):
        obj = self.context["view"].get_queryset().objects
        divsions = (
            obj.values_list("division", flat=True).distinct().order_by("division")
        )
        lineages = obj.values_list("lineage", flat=True).distinct().order_by("lineage")
        nextclade_pango = (
            obj.exclude(clade=None)
            .values_list("nextclade_pango", flat=True)
            .distinct()
            .order_by("nextclade_pango")
        )
        clade = (
            obj.exclude(clade=None)
            .values_list("clade", flat=True)
            .distinct()
            .order_by("clade")
        )
        # deletions = list(
        #     obj.values_list("aadeletions", flat=True).exclude(aadeletions=None)
        # )
        # deletions_data = []
        # for i in deletions:
        #     deletions_data.extend(i.split(","))
        # mutations = list(
        #     obj.values_list("aasubstitutions", flat=True).exclude(aasubstitutions=None)
        # )
        # mutations_data = []
        # for i in mutations:
        #     mutations_data.extend(i.split(","))
        data = {
            "clade": clade,
            "divsions": divsions,
            "lineages": lineages,
            "nextclade_pango": nextclade_pango,
            # "deletions": sorted(list(set(deletions_data))),
            # "mutations": sorted(list(set(mutations_data))),
        }
        return data


class CombinedAutoCompleteView(generics.GenericAPIView):
    queryset = QueryHubModel
    serializer_class = CombinedAutoCompleteSerializer

    def post(self, request, *args, **kwargs):
        self.serializer = self.get_serializer(data=request.data)
        if self.serializer.is_valid():
            return Response(self.serializer.validated_data)
        return Response(
            create_uniform_response(self.serializer.errors),
            status=status.HTTP_406_NOT_ACCEPTABLE,
        )
