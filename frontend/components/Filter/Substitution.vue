<template>
	<b-field expanded label="Amino acid substitution">
		<b-taginput
			rounded
			ellipsis
			autocomplete
			icon="filter"
			v-model="tags"
			:data="filtered"
			type="is-yellow"
			@typing="Filtering"
			close-type="is-dark"
			:placeholder="tags.length ? '' : 'Type amino acid substitution'"
		/>
	</b-field>
</template>

<script>
import FuzzySet from 'fuzzyset'
import { map, filter } from 'lodash'

export default {
	data: () => ({
		fs: null,
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
			this.state = await this.$axios.$post('/autocomplete/substitution/')
			this.fs = FuzzySet(this.state, true, 2, 5)
		})
	},
}
</script>

<style scoped></style>
