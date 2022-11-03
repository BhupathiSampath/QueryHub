<template>
	<div class="font-family-averta">
		<CommonNavBar />
		<Nuxt />
		<CommonFooter />
	</div>
</template>

<script>
export default {
	data: () => ({}),
	components: {},
	methods: {},
	mounted() {
		this.$nextTick(() => {
			// this.$store.dispatch('autocomplete/GetStateNames')
			// this.$store.dispatch('autocomplete/GetCladeNames')
			// this.$store.dispatch('autocomplete/GetLineageNames')
		})
	},
}
</script>

<style scoped></style>
