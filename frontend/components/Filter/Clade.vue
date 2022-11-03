<template>
	<b-field expanded label="Clade">
		<b-taginput
			rounded
			ellipsis
			autocomplete
			open-on-focus
			v-model="tags"
			icon="magnify"
			type="is-turquoise"
			:data="filtered"
			close-type="is-dark"
			@typing="Filtering"
			placeholder="Type a clade name"
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
			this.state = await this.$axios.$post('/autocomplete/nextclade/')
			this.filtered = this.state
		})
	},
}
</script>

<style scoped></style>
