<template>
	<div>
		<div class="columns is-variable is-1">
			<div class="column is-10">
				<!-- 				<b-field expanded>
					<b-input
						type="search"
						icon="magnify"
						v-model="general_query"
						placeholder="Enter search query"
					/>
				</b-field> -->
				<b-field expanded>
					<b-taginput
						rounded
						ellipsis
						id="ignore"
						type="is-info"
						icon="magnify"
						v-model="search"
						placeholder="Enter search query"
					>
					</b-taginput>
				</b-field>
			</div>
			<div class="column has-text-centered">
				<b-button type="is-info" expanded icon-left="magnify" label="Search" @click="Search" />
			</div>
		</div>

		<b-button
			type="is-light"
			label="Advanced Search"
			@click="ActivateAdvancedFilter"
			:icon-left="activate_filter ? 'chevron-up' : 'chevron-down'"
		/>

		<div class="columns is-variable is-1 py-2 is-multiline" v-show="activate_filter">
			<div class="column is-3">
				<FilterPangolineage v-model="pangolineage" :options="pangolineage_name" />
			</div>
			<div class="column is-3">
				<FilterNextcladelineage v-model="nextcladelineage" :options="nextcladelineage_name" />
			</div>
			<div class="column is-3">
				<FilterClade v-model="clade" :options="nextclade_name" />
			</div>
			<div class="column is-3">
				<FilterState v-model="state" :options="state_name" />
			</div>
			<div class="column is-6">
				<FilterSubstitution v-model="substitution" :options="substitution_name" />
			</div>
			<div class="column is-6">
				<FilterDeletion v-model="deletion" :options="deletion_name" />
			</div>
			<!-- 			<div class="column is-5">
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
				<b-field label="Date calculated from last date">
					<b-switch :value="false" type="is-info"> True </b-switch>
				</b-field>
			</div> -->
			<div class="column has-text-centered mt-4">
				<b-button type="is-dark" icon-left="check-outline" label="Apply filter" @click="Search" />
				<b-button type="is-dark" icon-left="filter-remove-outline" label="Clear filter" @click="Clear" />
			</div>
		</div>

		<div class="mt-2 has-text-weight-semibold">
			<div class="pb-2">Example search</div>
			<b-button type="is-info is-light" @click="RunExample(1)">Example 1 </b-button>
			<b-button type="is-info is-light" @click="RunExample(2)">Example 2</b-button>
			<b-button type="is-info is-light" @click="RunExample(3)">Example 3</b-button>
			<b-button type="is-info is-light" @click="RunExample(4)">Example 4</b-button>
		</div>
	</div>
</template>

<script>
import { mapFields } from 'vuex-map-fields'

export default {
	data: () => ({
		general_query: '',
		activate_filter: false,
	}),
	computed: {
		...mapFields('autocomplete', [
			'state_name',
			'deletion_name',
			'nextclade_name',
			'pangolineage_name',
			'substitution_name',
			'nextcladelineage_name',
		]),
		...mapFields([
			'filters.clade',
			'filters.state',
			'filters.dates',
			'filters.search',
			'filters.deletion',
			'filters.pangolineage',
			'filters.substitution',
			'filters.nextcladelineage',
		]),
	},
	methods: {
		ActivateAdvancedFilter() {
			this.activate_filter = !this.activate_filter
		},
		async Search() {
			const loading = this.$vs.loading()
			await this.$store.dispatch('UpdateTable')
			await this.$store.dispatch('GetStateGraph')
			await this.$store.dispatch('GetSubstitutionGraph')
			await this.$store.dispatch('GetSequenceWeeklyGraph')
			loading.close()
		},
		Clear() {
			this.clade = []
			this.state = []
			this.dates = []
			this.deletion = []
			this.pangolineage = []
			this.substitution = []
			this.nextcladelineage = []
		},
		RunExample(example_type) {
			this.activate_filter = this.activate_filter ? this.activate_filter : true
			switch (example_type) {
				case 1:
					this.clade = ['21A (Delta)']
					break
				case 2:
					this.clade = ['22B (Omicron)']
					this.pangolineage = ['BF.1', 'BF.2', 'BF.3', 'BF.4', 'BF.5']
					break
				case 3:
					this.clade = ['22B (Omicron)']
					this.nextcladelineage = ['BF.1', 'BF.2']
					this.pangolineage = ['BF.1', 'BF.2', 'BF.3', 'BF.4', 'BF.5']
					break
				case 4:
					this.pangolineage = ['BF.7']
					this.clade = ['22B (Omicron)']
					this.nextcladelineage = ['BF.7']
					this.substitution = ['ORF1a:L3027F', 'ORF1a:T3090I', 'ORF1a:T3255I']
					break
				default:
			}
		},
	},
	mounted() {
		this.$nextTick(() => {})
	},
}
</script>

<style scoped></style>
