<template>
	<b-field expanded label="Pangolin assigned lineage">
		<b-taginput
			rounded
			ellipsis
			autocomplete
			open-on-focus
			v-model="tags"
			icon="magnify"
			type="is-blue"
			:data="filtered"
			@typing="Filtering"
			close-type="is-dark"
			placeholder="Type a lineage name"
		/>
	</b-field>
</template>

<script>
export default {
	data: () => ({
		tags: [],
		state: [],
		filtered: [],
	}),
	components: {},
	methods: {
		Filtering(text) {
			this.filtered = this.state.filter((d) => d.toString().toLowerCase().indexOf(text.toLowerCase()) >= 0)
		},
	},
	mounted() {
		this.$nextTick(async () => {
			this.state = await this.$axios.$post('/autocomplete/pangolineage/')
			this.filtered = this.state
		})
	},
}
</script>

<style scoped></style>
