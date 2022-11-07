<template>
	<div>
		<section class="section">
			<div class="box">
				<FilterManager />
			</div>
		</section>

		<section class="section timeline-design">
			<div class="box">
				<GraphBar
					:chartdata="state"
					v-if="page_loaded"
					:formatter="StateFormatter"
					header="Sequence distribution (State)"
				/>
			</div>
		</section>

		<section class="section timeline-design">
			<div class="box">
				<div class="column has-text-right">
					<b-field>
						<b-switch type="is-dark" true-value="Weekly" false-value="Monthly" v-model="mode">
							Change to {{ mode == 'Monthly' ? 'Weekly' : 'Monthly' }}
						</b-switch>
					</b-field>
				</div>
				<GraphBar
					v-if="page_loaded"
					:axislabel="false"
					:chartdata="seq_week"
					:header="`Sequence distribution (${mode})`"
				/>
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
						<vs-pagination color="#065f9e" v-model="page" :length="total_pages" />
					</template>
				</vs-table>
			</div>
		</section>

		<!-- 		<section class="section timeline-design" v-for="item in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]" :key="item">
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
		</section> -->
	</div>
</template>

<script>
import { mapFields } from 'vuex-map-fields'

export default {
	data: () => ({
		page_loaded: false,
	}),
	watch: {
		async page(value) {
			const loading = this.$vs.loading({
				target: this.$refs.table_loader,
			})
			await this.$store.dispatch('UpdateTable')
			loading.close()
		},
		async mode(value) {
			const loading = this.$vs.loading()
			await this.$store.dispatch('GetSequenceWeeklyGraph')
			loading.close()
		},
	},
	computed: {
		...mapFields([
			'table_data',
			'total_pages',
			'filters.page',
			'filters.mode',
			'graphs.state',
			'graphs.seq_week',
			'graphs.state_graph_loaded',
			'graphs.seq_week_graph_loaded',
		]),
		RenamedStateLabel() {
			let rename = {
				AP: 'Andhra Pradesh',
				AR: 'Arunachal Pradesh',
				AS: 'Assam',
				BR: 'Bihar',
				CT: 'Chhattisgarh',
				GA: 'Goa',
				GJ: 'Gujarat',
				HR: 'Haryana',
				HP: 'Himachal Pradesh',
				JH: 'Jharkhand',
				KA: 'Karnataka',
				KL: 'Kerala',
				MP: 'Madhya Pradesh',
				MH: 'Maharashtra',
				MN: 'Manipur',
				ML: 'Meghalaya',
				MZ: 'Mizoram',
				NL: 'Nagaland',
				OR: 'Odisha',
				PB: 'Punjab',
				RJ: 'Rajasthan',
				SK: 'Sikkim',
				TN: 'Tamil Nadu',
				TG: 'Telangana',
				TR: 'Tripura',
				UT: 'Uttarakhand',
				UP: 'Uttar Pradesh',
				WB: 'West Bengal',
				AN: 'Andaman and Nicobar Islands',
				CH: 'Chandigarh',
				DN: 'Dadra and Nagar Haveli and Daman and Diu',
				DL: 'Delhi',
				JK: 'Jammu and Kashmir',
				LA: 'Ladakh',
				LD: 'Lakshadweep',
				PY: 'Puducherry',
			}
			let output = map(this.state, (d) => {
				return { name: rename[d.label], value: d.value }
			})
			return output
		},
	},
	methods: {
		StateFormatter(params) {
			let rename = {
				AP: 'Andhra Pradesh',
				AR: 'Arunachal Pradesh',
				AS: 'Assam',
				BR: 'Bihar',
				CT: 'Chhattisgarh',
				GA: 'Goa',
				GJ: 'Gujarat',
				HR: 'Haryana',
				HP: 'Himachal Pradesh',
				JH: 'Jharkhand',
				KA: 'Karnataka',
				KL: 'Kerala',
				MP: 'Madhya Pradesh',
				MH: 'Maharashtra',
				MN: 'Manipur',
				ML: 'Meghalaya',
				MZ: 'Mizoram',
				NL: 'Nagaland',
				OR: 'Odisha',
				PB: 'Punjab',
				RJ: 'Rajasthan',
				SK: 'Sikkim',
				TN: 'Tamil Nadu',
				TG: 'Telangana',
				TR: 'Tripura',
				UT: 'Uttarakhand',
				UP: 'Uttar Pradesh',
				WB: 'West Bengal',
				AN: 'Andaman and Nicobar Islands',
				CH: 'Chandigarh',
				DN: 'Dadra and Nagar Haveli and Daman and Diu',
				DL: 'Delhi',
				JK: 'Jammu and Kashmir',
				LA: 'Ladakh',
				LD: 'Lakshadweep',
				PY: 'Puducherry',
			}
			return `<b>${rename[params[0].name]} (${params[0].name})</b> : ${params[0].value}`
		},
	},
	mounted() {
		this.$nextTick(() => {
			this.page_loaded = true
		})
	},
}
</script>

<style scoped></style>
