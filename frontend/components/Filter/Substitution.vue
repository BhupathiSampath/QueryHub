<template>
	<b-field expanded label="Amino acid substitution">
		<b-taginput
			rounded
			ellipsis
			autocomplete
			v-model="tags"
			icon="magnify"
			:data="filtered"
			type="is-yellow"
			close-type="is-dark"
			@typing="Filtering"
			placeholder="Type amino acid substitution"
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
			this.state = await this.$axios.$post('/autocomplete/substitution/')
			this.filtered = this.state
		})
	},
}
</script>

<style scoped></style>
