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
        df = pd.read_csv(file, sep="\t", header=0, low_memory=False)
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
                "privateNucMutations.labeledSubstitutions": "privateNucMutations_labeledSubstitutions",
                "privateNucMutations.unlabeledSubstitutions": "privateNucMutations_unlabeledSubstitutions",
                "privateNucMutations.totalLabeledSubstitutions": "privateNucMutations_totalLabeledSubstitutions",
                "privateNucMutations.totalPrivateSubstitutions": "privateNucMutations_totalPrivateSubstitutions",
                "privateNucMutations.totalUnlabeledSubstitutions": "privateNucMutations_totalUnlabeledSubstitutions",
            },
            inplace=True,
        )
        df.loc[df.collection_week == "W52-2022", "collection_week"] = "W01-2022"
        engine = create_engine("sqlite:///database/db.sqlite3")

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


# dataframe column names which are remains same

# "tag": "tag",
# "age": "age",
# "sex": "sex",
# "date": "date",
# "host": "host",
# "note": "note",
# "clade": "clade",
# "title": "title",
# "virus": "virus",
# "region": "region",
# "length": "length",
# "strain": "strain",
# "lab_id": "lab_id",
# "missing": "missing",
# "authors": "authors",
# "lineage": "lineage",
# "segment": "segment",
# "country": "country",
# "division": "division",
# "location": "location",
# "qc_status": "qc_status",
# "deletions": "deletions",
# "paper_url": "paper_url",
# "nonACGTNs": "non_ACGTNs",
# "insertions": "insertions",
# "scorpio_call": "scorpio_call",
# "substitutions": "substitutions",
# "gisaid_epi_isl": "gisaid_epi_isl",
# "submitting_lab": "submitting_lab",
# "date_submitted": "date_submitted",
# "scorpio_support": "scorpio_support",
# "last_vaccinated": "last_vaccinated",
# "collection_week": "collection_week",
# "originating_lab": "originating_lab",
# "region_exposure": "region_exposure",
# "scorpio_conflict": "scorpio_conflict",
# "collection_month": "collection_month",
# "scorpio_conflict": "scorpio_conflict",
# "country_exposure": "country_exposure",
# "division_exposure": "division_exposure",
# "genbank_accession": "genbank_accession",
# "purpose_of_sequencing": "purpose_of_sequencing",
