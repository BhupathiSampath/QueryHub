from django.db.models import Count
from queryhub.models import QueryHubModel
from rest_framework.response import Response
from queryhub.api.utils import create_uniform_response
from queryhub.api.tasks import text_search, advenced_filter
from rest_framework import generics, exceptions, serializers, status


class WeekMonthCountSerializer(serializers.Serializer):
    def validate(self, value):
        request = self.context.get("request").data
        date = request.get("date")
        days = request.get("days")
        mode = request.get("mode")
        clade = request.get("clade")
        page = request.get("page", 1)
        search = request.get("search")
        strain = request.get("strain")
        present = request.get("present")
        division = request.get("state")
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
        if mode == "Weekly":
            obj = (
                obj.values("collection_week")
                .annotate(Count("strain", distinct=True))
                .order_by("date__year", "date__week")
            )
            return self.RenameKeys(list(obj), "collection_week", "strain__count")
        else:
            obj = (
                obj.values("collection_month")
                .annotate(Count("strain", distinct=True))
                .order_by("date__year", "date__month")
            )
            return self.RenameKeys(list(obj), "collection_month", "strain__count")

    @staticmethod
    def RenameKeys(obj, label, value):
        return [{"label": item[label], "value": item[value]} for item in obj]


class WeekMonthCountView(generics.GenericAPIView):
    serializer_class = WeekMonthCountSerializer

    def post(self, request, *args, **kwargs):
        self.serializer = self.get_serializer(data=request.data)
        if self.serializer.is_valid():
            return Response(self.serializer.validated_data)
        return Response(
            create_uniform_response(self.serializer.errors),
            status=status.HTTP_406_NOT_ACCEPTABLE,
        )
