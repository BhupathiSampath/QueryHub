<template>
	<b-field expanded label="State">
		<b-taginput
			rounded
			ellipsis
			autocomplete
			open-on-focus
			icon="filter"
			v-model="tags"
			type="is-green"
			:data="filtered"
			@typing="Filtering"
			close-type="is-dark"
			:placeholder="tags.length ? '' : 'Type a state name'"
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
			this.state = await this.$axios.$post('/autocomplete/state/')
			this.filtered = this.state
		})
	},
}
</script>

<style scoped></style>
