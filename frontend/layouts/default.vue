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
		this.$nextTick(async () => {
			const loading = this.$vs.loading()
			this.$store.dispatch('autocomplete/GetCladeNames')
			this.$store.dispatch('autocomplete/GetPangolineageNames')
			this.$store.dispatch('autocomplete/GetNextcladelineageNames')
			this.$store.dispatch('autocomplete/GetStateNames')
			this.$store.dispatch('autocomplete/GetDeletionNames')
			await this.$store.dispatch('autocomplete/GetSubstitutionNames')
			loading.close()
		})
	},
}
</script>

<style scoped></style>
