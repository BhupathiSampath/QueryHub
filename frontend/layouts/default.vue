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
		// ToggleTheme() {
		// 	// const button = document.querySelector('.btn')

		// 	// MediaQueryList object
		// 	const useDark = window.matchMedia('(prefers-color-scheme: dark)')

		// 	// Toggles the "dark-mode" class based on if the media query matches
		// 	function toggleDarkMode(state) {
		// 		// Older browser don't support the second parameter in the
		// 		// classList.toggle method so you'd need to handle this manually
		// 		// if you need to support older browsers.
		// 		document.documentElement.classList.toggle('dark-mode', state)
		// 	}

		// 	// Initial setting
		// 	toggleDarkMode(useDark.matches)

		// 	// Listen for changes in the OS settings
		// 	useDark.addListener((evt) => toggleDarkMode(evt.matches))

		// 	// Toggles the "dark-mode" class on click
		// 	button.addEventListener('click', () => {
		// 		document.documentElement.classList.toggle('dark-mode')
		// 	})
		// },
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
