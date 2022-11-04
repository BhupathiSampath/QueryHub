<template>
	<b-field expanded>
		<template #label>
			Amino acid deletion
			<b-tooltip type="is-dark" label="Help text here for explanation">
				<b-icon size="is-small" icon="help-circle-outline"></b-icon>
			</b-tooltip>
		</template>
		<b-taginput
			rounded
			ellipsis
			autocomplete
			icon="filter"
			v-model="tags"
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
		options: { type: Array, required: true },
	},
	watch: {
		tags(value) {
			this.$emit('input', value)
		},
		options(value) {
			this.SettingUpFS()
		},
	},
	methods: {
		Filtering(text) {
			this.filtered = filter(map(this.fs.get(text), (d) => (d.length ? d[1] : '')))
		},
		SettingUpFS() {
			this.fs = FuzzySet(this.options, true, 3, 5)
		},
	},
	mounted() {
		this.$nextTick(async () => {})
	},
}
</script>

<style scoped></style>
