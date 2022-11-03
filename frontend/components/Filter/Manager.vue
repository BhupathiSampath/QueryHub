<template>
	<div>
		<div class="columns is-variable is-1">
			<div class="column is-10">
				<b-field expanded>
					<b-input
						type="search"
						icon="magnify"
						v-model="general_query"
						placeholder="Enter search query"
					/>
				</b-field>
			</div>
			<div class="column has-text-centered">
				<b-button type="is-info" expanded icon-left="magnify" label="Search" />
			</div>
		</div>
		<b-button type="is-text" label="Advanced Search" @click="ActivateAdvancedFilter" />

		<div class="columns is-variable is-1 py-2 is-multiline">
			<div class="column is-3">
				<FilterPangolineage />
			</div>
			<div class="column is-3">
				<FilterNextcladelineage />
			</div>
			<div class="column is-3">
				<FilterClade v-model="filters.clade" />
			</div>
			<div class="column is-3">
				<FilterState />
			</div>
			<div class="column is-6">
				<FilterSubstitution />
			</div>
			<div class="column is-6">
				<FilterDeletion />
			</div>
			<div class="column is-5">
				<b-field label="Select date range">
					<b-datepicker range v-model="dates" locale="en-IN" placeholder="Click to select..." />
				</b-field>
			</div>
			<div class="column is-5">
				<b-field label="Range selector" class="px-4">
					<b-slider
						rounded
						:min="0"
						:max="9"
						type="is-info"
						:tooltip="false"
						aria-label="Range selector"
					>
						<b-slider-tick :value="0">Last week</b-slider-tick>
						<b-slider-tick :value="1">2 week</b-slider-tick>
						<b-slider-tick :value="2">3 week</b-slider-tick>
						<b-slider-tick :value="3">Last Month</b-slider-tick>
						<b-slider-tick :value="4">2 Month</b-slider-tick>
						<b-slider-tick :value="5">3 Month</b-slider-tick>
						<b-slider-tick :value="6">4 Month</b-slider-tick>
						<b-slider-tick :value="7">5 Month</b-slider-tick>
						<b-slider-tick :value="8">6 Month</b-slider-tick>
						<b-slider-tick :value="9">Last Year</b-slider-tick>
					</b-slider>
				</b-field>
			</div>
			<div class="column is-2 has-text-centered">
				<b-field>
					<b-switch :value="true" type="is-info"> Default </b-switch>
				</b-field>
			</div>
		</div>
	</div>
</template>

<script>
// import { mapFields } from 'vuex-map-fields'

export default {
	data: () => ({
		general_query: '',
		activate_filter: false,
		filters: {
			clade: [],
			state: [],
			dates: [],
			deletion: [],
			pangolineage: [],
			substitution: [],
			nextcladelineage: [],
		},
	}),
	// computed: {
	// 	...mapFields('autocomplete', ['state_name', 'lineage_name']),
	// },
	components: {},
	methods: {
		ActivateAdvancedFilter() {
			this.activate_filter = !this.activate_filter
		},
		// FilteredLineages(text) {
		// 	this.lineage_name = this.lineage_name.filter(
		// 		(d) => d.toString().toLowerCase().indexOf(text.toLowerCase()) >= 0,
		// 	)
		// },
		// FilteredState(text) {
		// 	this.state_name.filtered = this.state_name.raw.filter(
		// 		(d) => d.toString().toLowerCase().indexOf(text.toLowerCase()) >= 0,
		// 	)
		// },
		// TestClick(label) {
		// 	console.log('Clicked on ', label)
		// },
	},
	mounted() {
		this.$nextTick(() => {})
	},
}
</script>

<style scoped></style>
