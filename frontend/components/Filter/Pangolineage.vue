<template>
	<b-field expanded label="Pangolin assigned lineage (add example*)">
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
			this.state = await this.$axios.$post('/autocomplete/pangolineage/')
			this.filtered = this.state
		})
	},
}
</script>

<style scoped></style>
