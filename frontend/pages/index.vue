<template>
	<div>
		<section class="section">
			<div class="box">
				<FilterManager />
			</div>
		</section>

		<section class="section timeline-design" v-for="item in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]" :key="item">
			<div class="box">
				<div class="field">
					<label class="label">Email</label>
					<div class="control">
						<input class="input" type="email" placeholder="e.g. alex@example.com" />
					</div>
				</div>

				<div class="field">
					<label class="label">Password</label>
					<div class="control">
						<input class="input" type="password" placeholder="********" />
					</div>
				</div>

				<button class="button is-info">Sign in</button>
				<b-tag rounded icon="account-check-outline">Rounded Tag</b-tag>
			</div>
		</section>
	</div>
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
