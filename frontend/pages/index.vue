<template>
	<div>
		<section class="section">
			<div class="box">
				<FilterManager />
			</div>
		</section>

		<section class="section timeline-design">
			<div class="box">
				<vs-table ref="table_loader">
					<template #thead>
						<vs-tr>
							<vs-th sort class="is-size-6">Sample name</vs-th>
							<vs-th sort class="is-size-6">State</vs-th>
							<vs-th sort class="is-size-6">Date</vs-th>
							<vs-th sort class="is-size-6">Pangolin</vs-th>
							<vs-th sort class="is-size-6">Nextclade lineage</vs-th>
							<vs-th sort class="is-size-6">Nextclade clade</vs-th>
						</vs-tr>
					</template>
					<template #tbody>
						<vs-tr v-for="(item, index) in table_data" :key="index">
							<vs-td class="is-size-6 has-text-centered">{{ item.strain }}</vs-td>
							<vs-td class="is-size-6 has-text-centered">{{ item.division }}</vs-td>
							<vs-td class="is-size-6 has-text-centered">{{ item.date }}</vs-td>
							<vs-td class="is-size-6 has-text-centered">{{ item.lineage }}</vs-td>
							<vs-td class="is-size-6 has-text-centered">{{ item.nextclade_pango }}</vs-td>
							<vs-td class="is-size-6 has-text-centered">{{ item.clade }}</vs-td>
						</vs-tr>
					</template>
					<template #footer>
						<vs-pagination v-model="page" :length="total_pages" />
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
import { mapFields } from 'vuex-map-fields'

export default {
	data: () => ({}),
	watch: {
		async page(value) {
			const loading = this.$vs.loading({
				target: this.$refs.table_loader,
			})
			await this.$store.dispatch('UpdateTable')
			loading.close()
		},
	},
	computed: {
		...mapFields(['table_data', 'total_pages']),
		...mapFields(['filters.page']),
	},
	methods: {},
	mounted() {
		this.$nextTick(() => {})
	},
}
</script>

<style scoped></style>
