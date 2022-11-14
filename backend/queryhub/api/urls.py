from .get_data import GetDataView
from django.urls import path, include
from .lineages import UniqeLineageCount
from .upload import UploadNextstrainView
from .monthly_sequences import MonthlySequencesView
from .weekly_who_label import LineageClassificationWeek
from .monthly_who_label import LineageClassificationMonth
from .weekly_lineage_distribution import LineageWeeklyView
from .monthly_lineage_distribution import LineageMonthlyView
from .lineage_classification import LineageClassificationView
from .state_wise_classification import StateLineageClassification
from queryhub.api.weekly_report.variant_status import VariantStatusView
from queryhub.api.weekly_report.submitting_labs_sequences import SubmittingLabView
from queryhub.api.weekly_report.region_wise_analysis import RegionwiseAnalysisView
from queryhub.api.weekly_report.last_fourmonths_sequences import LastFourMonthsView
from queryhub.api.weekly_report.region_wise_2022_analysis import Regionwisedata2022
from queryhub.api.weekly_report.week_wise_last_threemonths import WeeklyThreemonthsView
from queryhub.api.weekly_report.variant_status_by_states import (
    VariantStatusbyStatesView,
)
from queryhub.api.weekly_report.last_fourmonths_variants import (
    LastFourMonthsVariantView,
)
from queryhub.api.weekly_report.state_wise_last_threemonths import (
    StateWiseLastThreemonthsView,
)

from .graph.state_count import StateCountView
from .graph.week_month_count import WeekMonthCountView
from .autocomplete.states import StatesAutoCompleteView
from .autocomplete.nextclade import CladeAutoCompleteView
from .autocomplete.mutation import MutationAutoCompleteView
from .autocomplete.deletion import DeletionAutoCompleteView
from .autocomplete.pangolineage import LineageAutoCompleteView
from .autocomplete.nextcladepango import NextcladePangolinAutoCompleteView
from .autocomplete.combined import CombinedAutoCompleteView
from .frontend_stats import FrontendStatsView

urlpatterns = [
    path("query/", GetDataView.as_view(), name="get_data"),
    path("stats/", FrontendStatsView.as_view(), name="stats"),
    path("upload/", UploadNextstrainView.as_view(), name="upload"),
    path("lineages_count/", UniqeLineageCount.as_view(), name="lineages_count"),
    path(
        "lineage_classification/",
        LineageClassificationView.as_view(),
        name="lineage_classification",
    ),
    path(
        "monthly_classification/",
        LineageClassificationMonth.as_view(),
        name="monthly_classification",
    ),
    path(
        "weekly_classification/",
        LineageClassificationWeek.as_view(),
        name="weekly_classification",
    ),
    path(
        "monthly_sequences/",
        MonthlySequencesView.as_view(),
        name="monthly_sequences",
    ),
    path(
        "state_lin_classification/",
        StateLineageClassification.as_view(),
        name="state_lin_classification",
    ),
    path(
        "monthly_lineage/",
        LineageMonthlyView.as_view(),
        name="monthly_lineage",
    ),
    path(
        "weekly_lineage/",
        LineageWeeklyView.as_view(),
        name="weekly_lineage",
    ),
    path(
        "last_fourmonths/",
        LastFourMonthsView.as_view(),
        name="last_fourmonths",
    ),
    path(
        "submitting_labs/",
        SubmittingLabView.as_view(),
        name="submitting_labs",
    ),
    path(
        "state_wise_last_threemonths/",
        StateWiseLastThreemonthsView.as_view(),
        name="state_wise_last_threemonths",
    ),
    path(
        "variant_status/",
        VariantStatusView.as_view(),
        name="variant_status",
    ),
    path(
        "last_fourmonths_variant_status/",
        LastFourMonthsVariantView.as_view(),
        name="last_fourmonths_variant_status",
    ),
    path(
        "week_wise_last_threemonths/",
        WeeklyThreemonthsView.as_view(),
        name="week_wise_last_threemonths",
    ),
    path(
        "region_wise_analysis/",
        RegionwiseAnalysisView.as_view(),
        name="region_wise_analysis",
    ),
    path(
        "variant_status_by_states/",
        VariantStatusbyStatesView.as_view(),
        name="variant_status_by_states",
    ),
    path(
        "region_wise_analysis_2022/",
        Regionwisedata2022.as_view(),
        name="region_wise_analysis_2022",
    ),
    path(
        "graph/",
        include(
            [
                path(
                    "state-count/",
                    StateCountView.as_view(),
                    name="state_wise_count",
                ),
                path(
                    "sequence-count/",
                    WeekMonthCountView.as_view(),
                    name="week_or_month_wise_count",
                ),
            ]
        ),
    ),
    path(
        "autocomplete/",
        include(
            [
                path(
                    "state/",
                    StatesAutoCompleteView.as_view(),
                    name="state_auto_complete",
                ),
                path(
                    "pangolineage/",
                    LineageAutoCompleteView.as_view(),
                    name="lineage_auto_complete",
                ),
                path(
                    "substitution/",
                    MutationAutoCompleteView.as_view(),
                    name="mutation_auto_complete",
                ),
                path(
                    "deletion/",
                    DeletionAutoCompleteView.as_view(),
                    name="deletion_auto_complete",
                ),
                path(
                    "nextclade/",
                    CladeAutoCompleteView.as_view(),
                    name="clade_auto_complete",
                ),
                path(
                    "nextcladelineage/",
                    NextcladePangolinAutoCompleteView.as_view(),
                    name="nextclade_auto_complete",
                ),
                path(
                    "combined/",
                    CombinedAutoCompleteView.as_view(),
                    name="combined_auto_complete",
                ),
            ]
        ),
    ),
]
