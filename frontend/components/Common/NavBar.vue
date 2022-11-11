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
	components: {},
	methods: {},
	mounted() {
		this.$nextTick(() => {})
	},
}
</script>

<style scoped></style>
