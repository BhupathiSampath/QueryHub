import operator
import datetime
import numpy as np
from functools import reduce
from django.db.models import Q
from datetime import date, timedelta
from django.db.models import Prefetch
from queryhub.models import QueryHubModel
from rest_framework.response import Response
from rest_framework import generics, exceptions, serializers, status


class MutationAutoCompleteSerializer(serializers.Serializer):
    def validate(self, value):
        obj = list(
            QueryHubModel.objects.prefetch_related("aasubstitutions")
            .values_list("aasubstitutions", flat=True)
            .filter(~Q(aasubstitutions=None))
        )
        data = []
        for i in obj:
            if not i is None:
                data.extend(i.split(","))
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
