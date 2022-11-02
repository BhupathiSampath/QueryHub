<template>
	<b-field expanded label="State">
		<b-taginput
			rounded
			ellipsis
			autocomplete
			open-on-focus
			v-model="tags"
			icon="magnify"
			:data="filtered"
			type="is-green"
			close-type="is-dark"
			@typing="Filtering"
			placeholder="Type a state name"
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
			this.state = await this.$axios.$post('/autocomplete/state/')
			this.filtered = this.state
		})
	},
}
</script>

<style scoped></style>
