<template>
	<b-navbar shadow fixed-top spaced>
		<template #brand>
			<b-navbar-item tag="router-link" :to="{ path: '/' }">
				<span class="is-size-5 has-text-weight-bold">XPLORECoV2</span>
			</b-navbar-item>
		</template>

		<template #end>
			<b-navbar-item tag="div">
				<div class="buttons">
					<a class="button is-light"> Log in </a>
				</div>
			</b-navbar-item>
		</template>
	</b-navbar>
</template>

<script>
export default {
	data: () => ({}),
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
	methods: {},
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
