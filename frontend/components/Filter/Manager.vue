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
			</div>
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
			loading.close()
		},
	},
	mounted() {
		this.$nextTick(() => {})
	},
}
</script>

<style scoped></style>
