<template>
	<b-field expanded label="Nextclade assigned lineage">
		<b-taginput
			rounded
			ellipsis
			autocomplete
			open-on-focus
			v-model="tags"
			icon="magnify"
			type="is-cyan"
			:data="filtered"
			close-type="is-dark"
			@typing="Filtering"
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
			this.state = await this.$axios.$post('/autocomplete/nextcladelineage/')
			this.filtered = this.state
		})
	},
}
</script>

<style scoped></style>
