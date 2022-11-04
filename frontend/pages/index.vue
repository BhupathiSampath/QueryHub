<template>
	<div>
		<section class="section">
			<div class="box">
				<FilterManager />
			</div>
		</section>

		<section class="section timeline-design">
			<div class="box">
				<vs-table>
					<template #thead>
						<vs-tr>
							<vs-th sort class="is-size-6 has-text-centered">Sample name</vs-th>
							<vs-th sort class="is-size-6 has-text-centered">Pangolin</vs-th>
							<vs-th sort class="is-size-6 has-text-centered">Nextclade lineage</vs-th>
							<vs-th sort class="is-size-6 has-text-centered">Nextclade clade</vs-th>
							<vs-th sort class="is-size-6 has-text-centered">Substitution</vs-th>
							<vs-th sort class="is-size-6 has-text-centered">Deletion</vs-th>
						</vs-tr>
					</template>
					<template #tbody>
						<vs-tr v-for="item in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]" :key="item">
							<vs-td class="is-size-6 has-text-centered">1</vs-td>
							<vs-td class="is-size-6 has-text-centered">2</vs-td>
							<vs-td class="is-size-6 has-text-centered">3</vs-td>
							<vs-td class="is-size-6 has-text-centered">4</vs-td>
							<vs-td class="is-size-6 has-text-centered">5</vs-td>
							<vs-td class="is-size-6 has-text-centered">6</vs-td>
						</vs-tr>
					</template>
					<template #footer>
						<vs-pagination circle v-model="page" :length="current" />
					</template>
				</vs-table>
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
	data: () => ({
		page: 1,
		current: 15,
	}),
	watch: {
		page(value) {},
	},
	components: {},
	methods: {},
	mounted() {
		this.$nextTick(() => {})
	},
}
</script>

<style scoped></style>
