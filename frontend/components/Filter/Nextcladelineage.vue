<template>
	<b-field expanded label="Nextclade assigned lineage">
		<b-taginput
			rounded
			ellipsis
			autocomplete
			open-on-focus
			icon="filter"
			v-model="tags"
			type="is-cyan"
			:data="filtered"
			@typing="Filtering"
			close-type="is-dark"
			:placeholder="tags.length ? '' : 'Type a lineage name'"
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
			this.state = await this.$axios.$post('/autocomplete/nextcladelineage/')
			this.filtered = this.state
		})
	},
}
</script>

<style scoped></style>
