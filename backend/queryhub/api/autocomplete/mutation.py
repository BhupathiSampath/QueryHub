import operator
import datetime
from functools import reduce
from django.db.models import Q
from queryhub.models import QueryHubModel
from datetime import date, timedelta
from rest_framework.response import Response
from rest_framework import generics, exceptions, serializers, status


class MutationAutoCompleteSerializer(serializers.Serializer):
    def validate(self, value):
        obj = list(QueryHubModel.objects.values_list("aasubstitutions", flat=True))
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
