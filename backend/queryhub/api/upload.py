import pandas as pd
from rest_framework import status
from ..models import QueryHubModel
from rest_framework import generics
from sqlalchemy import create_engine
from rest_framework import serializers
from .utils import create_uniform_response
from rest_framework.response import Response


class UploadSerializer(serializers.Serializer):
    nextstrain_file = serializers.FileField()

    class Meta:
        model = QueryHubModel
        fields = None

    def validate(self, value):
        file = value.get("nextstrain_file")
        df = pd.read_csv(file, sep="\t", header=0)
        df.sort_values("date", inplace=True)
        df.rename(
            columns={
                "url": "urls",
                "WHO_label": "who_label",
                "nonACGTNs": "non_ACGTNs",
                "region_type": "region_type",
                "aaDeletions": "aadeletions",
                "frameShifts": "frame_shifts",
                "totalMissing": "total_missing",
                "aaSubstitutions": "aasubstitutions",
                "Nextclade_pango": "nextclade_pango",
                "totalInsertions": "totalinsertions",
                "totalNonACGTNs": "total_non_ACGTNs",
                "qc.overallStatus": "qc_overallStatus",
                "totalFrameShifts": "total_frame_shifts",
                "privateNucMutations.unlabeledSubstitutions": "privateNucMutations_unlabeledSubstitutions",
                "privateNucMutations.totalLabeledSubstitutions": "privateNucMutations_totalLabeledSubstitutions",
                "privateNucMutations.totalPrivateSubstitutions": "privateNucMutations_totalPrivateSubstitutions",
                "privateNucMutations.totalUnlabeledSubstitutions": "privateNucMutations_totalUnlabeledSubstitutions",
                "privateNucMutations.labeledSubstitutions": "privateNucMutations_labeledSubstitutions",
            },
            inplace=True,
        )
        df.loc[df.collection_week == "W52-2022", "collection_week"] = "W01-2022"
        engine = create_engine("sqlite:///db.sqlite3")

        QueryHubModel(
            df.to_sql(
                QueryHubModel._meta.db_table,
                con=engine,
                index=True,
                if_exists="replace",
            )
        )
        return value


class UploadNextstrainView(generics.CreateAPIView):
    serializer_class = UploadSerializer

    def post(self, request, *args, **kwargs):
        self.serializer = self.get_serializer(data=request.data)
        if self.serializer.is_valid():
            return self.get_response()
        return Response(
            create_uniform_response(self.serializer.errors),
            status=status.HTTP_406_NOT_ACCEPTABLE,
        )

    def get_response(self):
        data = {
            "code": "SUCCESS",
            "message": "Data uploaded successfully",
        }
        response = Response(data, status=status.HTTP_200_OK)
        return response
