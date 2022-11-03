<template>
	<b-field expanded label="Amino acid deletion">
		<b-taginput
			rounded
			ellipsis
			autocomplete
			v-model="tags"
			icon="magnify"
			:data="filtered"
			type="is-orange"
			close-type="is-dark"
			@typing="Filtering"
			placeholder="Type amino acid deletion"
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
			this.state = await this.$axios.$post('/autocomplete/deletion/')
			this.filtered = this.state
		})
	},
}
</script>

<style scoped></style>
