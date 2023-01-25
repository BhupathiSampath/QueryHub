<template>
	<b-navbar fixed-top spaced :class="ClassNavbar">
		<template #brand>
			<div class="is-relative">
				<DesignCircle :class="ClassCircle" />
				<b-navbar-item tag="router-link" :to="{ path: '/' }">
					<span :class="ClassText">XPLORECoV2</span>
				</b-navbar-item>
			</div>
		</template>

		<template #end>
			<!-- 			<b-navbar-item tag="div">
				<b-button type="is-light" expanded icon-left="theme-light-dark" @click="ChangeColor" />
			</b-navbar-item>

			<b-navbar-item tag="div">
				<b-button type="is-light" expanded label="Log in" />
			</b-navbar-item> -->
		</template>
	</b-navbar>
</template>

<script>
export default {
	data: () => ({
		theme: 'light',
	}),
	props: {
		transparent: { type: Boolean, required: true },
	},
	computed: {
		ClassNavbar() {
			return this.transparent ? 'is-clipped no-shadow' : 'is-clipped has-shadow'
		},
		ClassText() {
			return this.$device.isDesktop
				? 'is-size-5 has-text-weight-bold mt-1'
				: 'is-size-5 has-text-weight-bold mt-1 shift-text'
		},
		ClassCircle() {
			return this.$device.isDesktop ? 'shift-circle' : 'shift-circle-mobile'
		},
	},
	methods: {
		ChangeColor() {
			// const hasSysDarkClass = document.body.classList.contains('systemDarkPreference')
			// console.log(hasSysDarkClass)
			// const a = window.matchMedia('(prefers-color-scheme: dark)')
			// console.log((a.matches = false))
			// const useDark = window.matchMedia('(prefers-color-scheme: dark)')
			// function toggleDarkMode(state) {
			// 	document.documentElement.classList.toggle('dark-mode', state)
			// }
			// toggleDarkMode(useDark.matches)
			// console.log(document.documentElement.classList)
			this.theme = this.theme == 'dark' ? 'light' : 'dark'
			if (this.theme == 'dark') {
				document.documentElement.classList.add('dark')
			} else {
				document.documentElement.classList.remove('dark')
			}
			// if (this.theme == 'dark') {
			// } else {
			// 	document.documentElement.classList.remove('dark')
			// 	this.theme = 'light'
			// }
			// window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (event) => {
			// 	const newColorScheme = event.matches ? 'dark' : 'light'
			// 	// console.log()
			// })
			// localStorage.setItem('theme', payload)
		},
	},
	mounted() {
		this.$nextTick(() => {})
	},
}
</script>

<style scoped>
.shift-circle {
	top: -220%;
	left: -161%;
	height: 540%;
	position: absolute;
}
.shift-circle-mobile {
	top: -220%;
	left: -115%;
	height: 540%;
	position: absolute;
}
.shift-text {
	padding-left: 50px;
}
</style>
