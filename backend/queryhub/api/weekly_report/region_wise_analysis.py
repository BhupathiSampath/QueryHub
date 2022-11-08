from itertools import groupby
from django.db.models import Count
from queryhub.models import QueryHubModel
from rest_framework.response import Response
from ..utils import create_uniform_response, weekly_report_stacked
from rest_framework import generics, exceptions, serializers, status


def key_func(k):
    return k["region_type"]


class RegionwiseAnalysisSerializer(serializers.Serializer):
    def validate(self, value):
        a = []
        b = []
        c = {}
        d = {}
        QuerySet = (
            QueryHubModel.objects.filter(date__gte="2021-01-01")
            .values("region_type", "collection_week", "who_label")
            .annotate(Count("strain", distinct=True))
            .order_by("date__year")
        )
        QuerySet = sorted(QuerySet, key=key_func)
        for key, value in groupby(QuerySet, key_func):
            b.append(list(value))
            for i in b:
                c[key] = i
        for i in c:
            for items in c[i]:
                del items["region_type"]
            d[i] = weekly_report_stacked(c[i])
        labels = QueryHubModel.objects.values_list("who_label", flat=True).distinct()
        for i in d.values():
            for j in sorted(labels):
                if not any(d["who_label"] == j for d in i["who_label"]):
                    ad = {}
                    ad["who_label"] = j
                    ad["value"] = [0] * len(i["who_label"][0]["value"])
                    ad["value1"] = [0.0] * len(i["who_label"][0]["value"])
                    i["who_label"].append(ad)
            i["who_label"] = sorted(i["who_label"], key=lambda d: d["who_label"])
        return d


class RegionwiseAnalysisView(generics.GenericAPIView):
    serializer_class = RegionwiseAnalysisSerializer

    def post(self, request, *args, **kwargs):
        self.serializer = self.get_serializer(data=request.data)
        if self.serializer.is_valid():
            return Response(self.serializer.validated_data)
        return Response(
            create_uniform_response(self.serializer.errors),
            status=status.HTTP_406_NOT_ACCEPTABLE,
        )
