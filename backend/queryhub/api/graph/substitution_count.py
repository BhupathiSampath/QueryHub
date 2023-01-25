import itertools, re, numpy
from collections import Counter
from django.db.models import Count
from queryhub.models import QueryHubModel
from rest_framework.response import Response
from queryhub.api.utils import create_uniform_response
from queryhub.api.tasks import TextSearch, AdvancedFilter
from rest_framework import generics, exceptions, serializers, status


class SubstitutionCountSerializer(serializers.Serializer):
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
            obj = TextSearch(search, obj)
        obj = AdvancedFilter(
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
        obj = obj.order_by("?").values("substitutions")[:50][::-1]
        return_data = []
        for item in obj:
            if item["substitutions"]:
                return_data.append(item["substitutions"].split(","))

        return self.RenameKeys(dict(Counter(list(itertools.chain(*return_data)))))

    @staticmethod
    def RenameKeys(obj):
        temp = {"line": [], "scatter": []}
        max_val = obj[max(obj.keys(), key=(lambda k: obj[k]))]
        for index, value in obj.items():
            temp["line"].append([0, 0])
            position = re.findall(r"\d+", index)[0]
            temp["line"].append(
                [int(numpy.interp(value, [1, max_val], [60, 100])), int(position)]
            )
            temp["scatter"].append(
                [int(numpy.interp(value, [1, max_val], [60, 100])), int(position)]
            )
        return temp


class SubstitutionCountView(generics.GenericAPIView):
    serializer_class = SubstitutionCountSerializer

    def post(self, request, *args, **kwargs):
        self.serializer = self.get_serializer(data=request.data)
        if self.serializer.is_valid():
            return Response(self.serializer.validated_data)
        return Response(
            create_uniform_response(self.serializer.errors),
            status=status.HTTP_406_NOT_ACCEPTABLE,
        )
