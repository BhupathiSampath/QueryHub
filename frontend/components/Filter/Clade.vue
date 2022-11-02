<template>
	<b-field expanded label="Clade">
		<b-taginput
			rounded
			ellipsis
			autocomplete
			open-on-focus
			v-model="tags"
			icon="magnify"
			:data="filtered"
			type="is-turquoise"
			@typing="Filtering"
			close-type="is-dark"
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
	props: {
		value: { type: Array, required: true },
	},
	watch: {
		tags(value) {
			this.$emit('input', value)
		},
	},
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
