from django.urls import path

from .get_data import GetDataView
from .lineages import UniqeLineageCount
from .upload import UploadNextstrainView
from .weekly_sequences import WeeklySequencesView
from .monthly_sequences import MonthlySequencesView
from .state_wise_sequences import StateSequencesView
from .weekly_who_label import LineageClassificationWeek
from .states_auto_complete import StatesAutoCompleteView
from .monthly_who_label import LineageClassificationMonth
from .lineage_auto_complete import LineageAutoCompleteView
from .weekly_lineage_distribution import LineageWeeklyView
from .mutation_auto_complete import MutationAutoCompleteView
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

urlpatterns = [
    path("get_data/", GetDataView.as_view(), name="get_data"),
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
        "weekly_sequences/",
        WeeklySequencesView.as_view(),
        name="weekly_sequences",
    ),
    path(
        "state_sequences/",
        StateSequencesView.as_view(),
        name="state_sequences",
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
        "autocomplete/",
        include(
            [
                path(
                    "state/",
                    StatesAutoCompleteView.as_view(),
                    name="state_auto_complete",
                ),
                path(
                    "lineage/",
                    LineageAutoCompleteView.as_view(),
                    name="lineage_auto_complete",
                ),
                path(
                    "mutation/",
                    MutationAutoCompleteView.as_view(),
                    name="mutation_auto_complete",
                ),
            ]
        ),
    ),
]
