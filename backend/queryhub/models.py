from django.db import models
from django.db.models import CharField, Model

# Create your models here.


class QueryHubModel(models.Model):
    index = models.BigIntegerField(primary_key=True)
    date = models.DateField(default=None, blank=True, null=True)
    date_submitted = models.DateField(default=None, blank=True, null=True)
    age = models.CharField(max_length=300, default=None, blank=True, null=True)
    sex = models.CharField(max_length=300, default=None, blank=True, null=True)
    host = models.CharField(max_length=300, default=None, blank=True, null=True)
    urls = models.CharField(max_length=300, default=None, blank=True, null=True)
    clade = models.CharField(max_length=300, default=None, blank=True, null=True)
    title = models.CharField(max_length=300, default=None, blank=True, null=True)
    virus = models.CharField(max_length=300, default=None, blank=True, null=True)
    region = models.CharField(max_length=300, default=None, blank=True, null=True)
    lab_id = models.CharField(max_length=300, default=None, blank=True, null=True)
    strain = models.CharField(max_length=300, default=None, blank=True, null=True)
    length = models.CharField(max_length=300, default=None, blank=True, null=True)
    lineage = models.CharField(max_length=225, default=None, blank=True, null=True)
    missing = models.CharField(max_length=300, default=None, blank=True, null=True)
    authors = models.CharField(max_length=300, default=None, blank=True, null=True)
    segment = models.CharField(max_length=300, default=None, blank=True, null=True)
    country = models.CharField(max_length=300, default=None, blank=True, null=True)
    division = models.CharField(max_length=300, default=None, blank=True, null=True)
    location = models.CharField(max_length=300, default=None, blank=True, null=True)
    qc_status = models.CharField(max_length=225, default=None, blank=True, null=True)
    deletions = models.CharField(max_length=300, default=None, blank=True, null=True)
    paper_url = models.CharField(max_length=300, default=None, blank=True, null=True)
    who_label = models.CharField(max_length=300, default=None, blank=True, null=True)
    non_ACGTNs = models.CharField(max_length=300, default=None, blank=True, null=True)
    aadeletions = models.CharField(max_length=300, default=None, blank=True, null=True)
    insertions = models.CharField(max_length=300, default=None, blank=True, null=True)
    region_type = models.CharField(max_length=300, default=None, blank=True, null=True)
    frame_shifts = models.CharField(max_length=300, default=None, blank=True, null=True)
    total_missing = models.CharField(
        max_length=300, default=None, blank=True, null=True
    )
    substitutions = models.CharField(
        max_length=300, default=None, blank=True, null=True
    )
    submitting_lab = models.CharField(
        max_length=300, default=None, blank=True, null=True
    )
    gisaid_epi_isl = models.CharField(
        max_length=300, default=None, blank=True, null=True
    )
    aasubstitutions = models.CharField(
        max_length=300, default=None, blank=True, null=True
    )
    # aasubstitutions = ListCharField(
    #     base_field=CharField(max_length=10),
    #     size=6,
    #     max_length=(6 * 11),
    # )
    nextclade_pango = models.CharField(
        max_length=300, default=None, blank=True, null=True
    )
    totalinsertions = models.CharField(
        max_length=300, default=None, blank=True, null=True
    )
    scorpio_support = models.CharField(
        max_length=225, default=None, blank=True, null=True
    )
    last_vaccinated = models.CharField(
        max_length=300, default=None, blank=True, null=True
    )
    collection_week = models.CharField(
        max_length=300, default=None, blank=True, null=True
    )
    originating_lab = models.CharField(
        max_length=300, default=None, blank=True, null=True
    )
    region_exposure = models.CharField(
        max_length=300, default=None, blank=True, null=True
    )
    total_non_ACGTNs = models.CharField(
        max_length=300, default=None, blank=True, null=True
    )
    collection_month = models.CharField(
        max_length=300, default=None, blank=True, null=True
    )
    scorpio_conflict = models.CharField(
        max_length=225, default=None, blank=True, null=True
    )
    country_exposure = models.CharField(
        max_length=300, default=None, blank=True, null=True
    )
    division_exposure = models.CharField(
        max_length=300, default=None, blank=True, null=True
    )
    genbank_accession = models.CharField(
        max_length=300, default=None, blank=True, null=True
    )
    total_frame_shifts = models.CharField(
        max_length=300, default=None, blank=True, null=True
    )
    purpose_of_sequencing = models.CharField(
        max_length=300, default=None, blank=True, null=True
    )
    privateNucMutations_totalLabeledSubstitutions = models.CharField(
        max_length=300, default=None, blank=True, null=True
    )
    privateNucMutations_totalPrivateSubstitutions = models.CharField(
        max_length=300, default=None, blank=True, null=True
    )
    privateNucMutations_totalUnlabeledSubstitutions = models.CharField(
        max_length=300, default=None, blank=True, null=True
    )
    privateNucMutations_unlabeledSubstitutions = models.CharField(
        max_length=300, default=None, blank=True, null=True
    )

    def __str__(self):
        return self.strain
