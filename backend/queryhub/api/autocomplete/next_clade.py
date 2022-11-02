from queryhub.models import QueryHubModel
from rest_framework.response import Response
from queryhub.api.utils import create_uniform_response
from rest_framework import generics, exceptions, serializers, status


class NextCladeAutoCompleteSerializer(serializers.Serializer):
    def validate(self, value):
        obj = self.context["view"].get_queryset().objects
        return (
            obj.values_list("nextclade_pango", flat=True)
            .distinct()
            .order_by("nextclade_pango")
        )


class NextCladeAutoCompleteView(generics.GenericAPIView):
    queryset = QueryHubModel
    serializer_class = NextCladeAutoCompleteSerializer

    def post(self, request, *args, **kwargs):
        self.serializer = self.get_serializer(data=request.data)
        if self.serializer.is_valid():
            return Response(self.serializer.validated_data)
        return Response(
            create_uniform_response(self.serializer.errors),
            status=status.HTTP_406_NOT_ACCEPTABLE,
        )
