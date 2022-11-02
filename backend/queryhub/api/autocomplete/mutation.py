import operator
import datetime
from functools import reduce
from django.db.models import Q
from queryhub.models import QueryHubModel
from datetime import date, timedelta
from rest_framework.response import Response
from rest_framework import generics, exceptions, serializers, status


class MutationAutoCompleteSerializer(serializers.ModelSerializer):
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
            "division",
            "lineage",
            "aasubstitutions",
            "nextclade_pango",
        )

    def validate(self, value):
        date = value.get("date")
        lineage = value.get("lineage")
        division = value.get("division")
        nextclade_pango = value.get("nextclade_pango")
        aasubstitutions = value.get("aasubstitutions")
        days = self.context.get("request").data.get("days")
        present = self.context.get("request").data.get("present")
        obj = QueryHubModel.objects
        if days and present == False:
            last_date = QueryHubModel.objects.values("date").latest("date")
            day = last_date["date"] - timedelta(days=int(days))
            obj = obj.filter(date__gte=day)
        if days and present == True:
            day = datetime.date.today() - timedelta(days=int(days))
            obj = obj.filter(date__gte=day)
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
        obj = list(obj.values_list("aasubstitutions", flat=True))
        data = []
        for i in obj:
            if not i is None:
                data.extend(i.split(","))
        data.append("None")
        return sorted(list(set(data)))


class MutationAutoCompleteView(generics.GenericAPIView):
    serializer_class = MutationAutoCompleteSerializer

    def post(self, request, *args, **kwargs):
        self.serializer = self.get_serializer(data=request.data)
        if self.serializer.is_valid():
            return Response(self.serializer.validated_data)
        return Response(
            create_uniform_response(self.serializer.errors),
            status=status.HTTP_406_NOT_ACCEPTABLE,
        )
