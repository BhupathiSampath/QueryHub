from django.db.models import Count
from queryhub.models import QueryHubModel
from rest_framework.response import Response
from ..utils import create_uniform_response, weekly_report_stacked
from rest_framework import generics, exceptions, serializers, status


class VariantStatusSerializer(serializers.Serializer):
    def validate(self, value):
        QuerySet = (
            QueryHubModel.objects.filter(
                date__gte="2021-01-01",
            )
            .values("collection_week", "who_label")
            .annotate(Count("strain", distinct=True))
            .order_by("date__year")
        )
        return weekly_report_stacked(QuerySet)


class VariantStatusView(generics.GenericAPIView):
    serializer_class = VariantStatusSerializer

    def post(self, request, *args, **kwargs):
        self.serializer = self.get_serializer(data=request.data)
        if self.serializer.is_valid():
            return Response(self.serializer.validated_data)
        return Response(
            create_uniform_response(self.serializer.errors),
            status=status.HTTP_406_NOT_ACCEPTABLE,
        )
