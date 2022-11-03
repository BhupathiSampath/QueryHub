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
			@typing="Filtering"
			close-type="is-dark"
			:placeholder="tags.length ? '' : 'Type amino acid deletion'"
		/>
	</b-field>
</template>

<script>
import FuzzySet from 'fuzzyset'
import { map, filter } from 'lodash'

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
			this.filtered = filter(map(this.fs.get(text), (d) => (d.length ? d[1] : '')))
		},
	},
	mounted() {
		this.$nextTick(async () => {
			this.state = await this.$axios.$post('/autocomplete/deletion/')
			this.fs = FuzzySet(this.state, true, 3, 5)
		})
	},
}
</script>

<style scoped></style>
