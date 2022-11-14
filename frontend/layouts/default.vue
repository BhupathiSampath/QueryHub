<template>
	<div class="font-family-averta">
		<CommonNavBar :transparent="transparent" />
		<Nuxt />
		<CommonFooter />
	</div>
</template>

<script>
export default {
	data: () => ({
		transparent: true,
	}),
	components: {},
	methods: {
		handleScroll() {
			if (window.scrollY > 20) {
				this.transparent = false
			} else {
				this.transparent = true
			}
		},
	},
	mounted() {
		this.$nextTick(async () => {
			const loading = this.$vs.loading()
			this.$store.dispatch('GetTable')
			this.$store.dispatch('GetStateGraph')
			this.$store.dispatch('GetSequenceWeeklyGraph')
			this.$store.dispatch('autocomplete/GetCladeNames')
			this.$store.dispatch('autocomplete/GetStateNames')
			this.$store.dispatch('autocomplete/GetPangolineageNames')
			this.$store.dispatch('autocomplete/GetDeletionNames')
			this.$store.dispatch('autocomplete/GetNextcladelineageNames')
			await this.$store.dispatch('autocomplete/GetSubstitutionNames')
			loading.close()
		})
	},
	created() {
		if (process.client) {
			window.addEventListener('scroll', this.handleScroll)
		}
	},
	destroyed() {
		if (process.client) {
			window.removeEventListener('scroll', this.handleScroll)
		}
	},
}
</script>

<style scoped></style>
