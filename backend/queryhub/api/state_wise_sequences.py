from django.db.models import Count
from ..models import QueryHubModel
from .utils import create_uniform_response
from rest_framework.response import Response
from .tasks import text_search, advenced_filter
from rest_framework import generics, exceptions, serializers, status


class StateSequencesSerializer(serializers.Serializer):
    def validate(self, value):
        request = self.context.get("request").data
        date = request.get("date")
        days = request.get("days")
        clade = request.get("clade")
        page = request.get("page", 1)
        search = request.get("search")
        strain = request.get("strain")
        present = request.get("present")
        division = request.get("state")
        lineage = request.get("pangolineage")
        aadeletions = request.get("deletion")
        nextclade_pango = request.get("nextcladelineage")
        aasubstitutions = request.get("substitution")
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
        obj = list(
            obj.values("division")
            .annotate(Count("strain", distinct=True))
            .order_by("-strain__count")
        )
        return self.RenameKeys(self.RenameStates(obj), "division", "strain__count")

    @staticmethod
    def RenameKeys(obj, label, value):
        return [{"label": item[label], "value": item[value]} for item in obj]

    @staticmethod
    def RenameStates(obj):
        rename = {
            "Andhra Pradesh": "AP",
            "Arunachal Pradesh": "AR",
            "Assam": "AS",
            "Bihar": "BR",
            "Chhattisgarh": "CT",
            "Goa": "GA",
            "Gujarat": "GJ",
            "Haryana": "HR",
            "Himachal Pradesh": "HP",
            "Jharkhand": "JH",
            "Karnataka": "KA",
            "Kerala": "KL",
            "Madhya Pradesh": "MP",
            "Maharashtra": "MH",
            "Manipur": "MN",
            "Meghalaya": "ML",
            "Mizoram": "MZ",
            "Nagaland": "NL",
            "Odisha": "OR",
            "Punjab": "PB",
            "Rajasthan": "RJ",
            "Sikkim": "SK",
            "Tamil Nadu": "TN",
            "Telangana": "TG",
            "Tripura": "TR",
            "Uttarakhand": "UT",
            "Uttar Pradesh": "UP",
            "West Bengal": "WB",
            "Andaman and Nicobar Islands": "AN",
            "Chandigarh": "CH",
            "Dadra and Nagar Haveli and Daman and Diu": "DN",
            "Delhi": "DL",
            "Jammu and Kashmir": "JK",
            "Ladakh": "LA",
            "Lakshadweep": "LD",
            "Puducherry": "PY",
        }
        for item in obj:
            item["division"] = rename[item["division"]]

        return obj


class StateSequencesView(generics.GenericAPIView):
    serializer_class = StateSequencesSerializer

    def post(self, request, *args, **kwargs):
        self.serializer = self.get_serializer(data=request.data)
        if self.serializer.is_valid():
            return Response(self.serializer.validated_data)
        return Response(
            create_uniform_response(self.serializer.errors),
            status=status.HTTP_406_NOT_ACCEPTABLE,
        )
