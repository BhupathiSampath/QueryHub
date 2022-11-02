from queryhub.models import QueryHubModel
from rest_framework.response import Response
from queryhub.api.utils import create_uniform_response
from rest_framework import generics, exceptions, serializers, status


class CladeAutoCompleteSerializer(serializers.Serializer):
    def validate(self, value):
        obj = self.context["view"].get_queryset().objects
        return (
            obj.exclude(clade=None)
            .values_list("clade", flat=True)
            .distinct()
            .order_by("clade")
        )


class CladeAutoCompleteView(generics.GenericAPIView):
    queryset = QueryHubModel
    serializer_class = CladeAutoCompleteSerializer

    def post(self, request, *args, **kwargs):
        self.serializer = self.get_serializer(data=request.data)
        if self.serializer.is_valid():
            return Response(self.serializer.validated_data)
        return Response(
            create_uniform_response(self.serializer.errors),
            status=status.HTTP_406_NOT_ACCEPTABLE,
        )
