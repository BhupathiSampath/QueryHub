<template>
	<div>
		<div class="columns is-variable is-1">
			<div class="column is-10">
				<b-field expanded>
					<b-input
						v-model="general_query"
						placeholder="Enter search query"
						type="search"
						icon="magnify"
					/>
				</b-field>
			</div>
			<div class="column has-text-centered">
				<b-button type="is-info" expanded icon-left="magnify" label="Search" />
			</div>
		</div>
		<b-button type="is-text" label="Advanced Search" @click="ActivateAdvancedFilter" />

		<div class="columns is-variable is-1 py-2 is-multiline">
			<div class="column is-4">
				<b-field expanded label="Pangolin">
					<b-input
						v-model="general_query"
						placeholder="Enter pangolin lineage"
						type="search"
						icon="magnify"
					/>
				</b-field>
			</div>
			<div class="column is-4">
				<b-field expanded label="Nextclade">
					<b-input
						v-model="general_query"
						placeholder="Enter nextclade clade"
						type="search"
						icon="magnify"
					/>
				</b-field>
			</div>
			<div class="column is-4">
				<b-field expanded label="State">
					<b-input v-model="general_query" placeholder="Enter state name" type="search" icon="magnify" />
				</b-field>
			</div>
			<div class="column is-6">
				<b-field expanded label="Substitution">
					<b-input
						v-model="general_query"
						placeholder="Enter nextclade clade"
						type="search"
						icon="magnify"
					/>
				</b-field>
			</div>
			<div class="column is-6">
				<b-field expanded label="Deletion">
					<b-input
						v-model="general_query"
						placeholder="Enter nextclade clade"
						type="search"
						icon="magnify"
					/>
				</b-field>
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
export default {
	data: () => ({
		dates: [],
		general_query: '',
		activate_filter: false,
	}),
	components: {},
	methods: {
		ActivateAdvancedFilter() {
			this.activate_filter = !this.activate_filter
		},
	},
	mounted() {
		this.$nextTick(() => {})
	},
}
</script>

<style scoped></style>
