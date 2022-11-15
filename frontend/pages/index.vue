<template>
	<div class="bg-design">
		<section class="section">
			<div class="box box-size is-clipped is-relative">
				<DesignCircle :class="ClassCircle" />
				<div class="column is-offset-2 is-10 has-text-justified">
					<!-- 					<span class="is-size-5 has-text-weight-bold has-background-white mt-1 is-block"
						>XPLORECoV2</span
					> -->
					Sunt duis fugiat velit dolore velit id laboris aliqua enim dolor enim qui fugiat et dolor ex
					cupidatat anim commodo eu sed dolore sed ut do qui velit reprehenderit pariatur et mollit in
					laborum do irure ut veniam nostrud voluptate elit in veniam officia cillum sunt mollit esse
					excepteur incididunt excepteur ex magna sed nostrud ut dolore labore excepteur mollit tempor
					magna nostrud velit aute sit laborum aliquip id nulla fugiat anim cillum ex et eiusmod elit sed
					sit culpa elit laboris proident deserunt in elit et deserunt culpa consectetur fugiat dolor
					velit amet voluptate sed sunt non commodo culpa qui esse ullamco minim qui nulla in laborum
					commodo irure duis ex enim veniam sint in velit proident ut cupidatat aliquip consectetur irure
					proident dolore id eu ut eu dolor qui consequat cupidatat eiusmod qui velit ut consectetur
					consectetur consequat et consequat consequat duis ullamco id ut enim in est aliquip qui aliqua
					consequat cillum veniam veniam ullamco magna duis duis adipisicing in enim aliquip exercitation
					veniam dolor magna ut est aliqua cillum dolore pariatur enim pariatur culpa adipisicing laboris
					tempor eiusmod adipisicing in minim aliquip non minim aute incididunt ut fugiat culpa mollit in
					sunt sit consequat sint qui commodo dolore eu laborum dolor tempor irure irure velit proident
					anim fugiat velit ut esse aliquip officia irure culpa magna consequat labore ea ex est tempor
					dolor id excepteur nulla ut pariatur exercitation labore deserunt veniam anim reprehenderit
					amet laborum veniam reprehenderit tempor eu in velit enim.
				</div>
			</div>
		</section>

		<section :class="ClassSection">
			<div class="box">
				<FilterManager />
				<div class="mt-2 has-text-weight-semibold">
					<div class="pb-2">Example search</div>
					<b-button type="is-info is-light">Example 1 </b-button>
					<b-button type="is-info is-light">Example 2</b-button>
					<b-button type="is-info is-light">Example 3</b-button>
					<b-button type="is-info is-light">Example 4</b-button>
				</div>
			</div>
		</section>

		<section :class="ClassSection">
			<div class="box">
				<div class="title is-5 has-text-centered has-text-grey-light">Data statistics</div>
				<nav class="level">
					<div class="level-item has-text-centered">
						<div>
							<p class="heading">Genomes Uploaded</p>
							<p class="title">{{ stats.total }}</p>
						</div>
					</div>
					<div class="level-item has-text-centered">
						<div>
							<p class="heading">Lineages Found</p>
							<p class="title">{{ stats.lineages }}</p>
						</div>
					</div>
					<div class="level-item has-text-centered">
						<div>
							<p class="heading">NextcladePango Found</p>
							<p class="title">{{ stats.nextcladepango }}</p>
						</div>
					</div>
					<div class="level-item has-text-centered">
						<div>
							<p class="heading">Clades Found</p>
							<p class="title">{{ stats.clade }}</p>
						</div>
					</div>
					<div class="level-item has-text-centered">
						<div>
							<p class="heading">States Covered</p>
							<p class="title">{{ stats.state }}</p>
						</div>
					</div>
					<div class="level-item has-text-centered">
						<div>
							<p class="heading">Filtered Set</p>
							<p class="title">{{ stats.filtered }}</p>
						</div>
					</div>
				</nav>
				<hr />
				<div class="title is-5 has-text-centered has-text-grey-light">Tool versions</div>
				<nav class="level">
					<div class="level-item has-text-centered" v-for="(tool, value) in version" :key="tool">
						<div>
							<p class="heading">{{ value }}</p>
							<p class="title">{{ tool }}</p>
						</div>
					</div>
				</nav>
			</div>
		</section>

		<section :class="ClassSection">
			<div class="box">
				<div class="column has-text-right">
					<b-field>
						<b-switch type="is-dark" true-value="Map" false-value="Bar" v-model="map_bar_switcher">
							Change to {{ map_bar_switcher == 'Map' ? 'Bar' : 'Map' }}
						</b-switch>
					</b-field>
				</div>
				<GraphBar
					:chartdata="state"
					:formatter="StateFormatter"
					header="Sequence distribution (State)"
					v-if="page_loaded && map_bar_switcher == 'Bar'"
				/>
				<GraphMap
					:chartdata="RenamedStateLabel"
					header="Sequence distribution (State)"
					v-if="page_loaded && map_bar_switcher == 'Map'"
				/>

				<!-- 				<div class="column has-text-centered">
					<div class="is-size-5 has-text-medium has-text-weight-semibold has-text-grey-dark">
						Sequence distribution (State)
					</div>
				</div>
				<div class="columns" v-if="page_loaded && state_graph_loaded">
					<div class="column">
						<GraphBar vertical :chartdata="state" :formatter="StateFormatter" />
					</div>
					<div class="column">
						<GraphMap :chartdata="RenamedStateLabel" />
					</div>
				</div> -->
			</div>
		</section>

		<section :class="ClassSection">
			<div class="box">
				<div class="column has-text-right">
					<b-field>
						<b-switch type="is-dark" true-value="Weekly" false-value="Monthly" v-model="mode">
							Change to {{ mode == 'Monthly' ? 'Weekly' : 'Monthly' }}
						</b-switch>
					</b-field>
				</div>
				<GraphBar
					:dosort="false"
					v-if="page_loaded"
					:axislabel="false"
					:chartdata="seq_week"
					:header="`Sequence distribution (${mode})`"
				/>
			</div>
		</section>

		<section :class="ClassSection">
			<div class="box">
				<vs-table ref="table_loader">
					<template #thead>
						<vs-tr>
							<vs-th sort class="is-size-6" @click="Sort($event)">Sample name</vs-th>
							<vs-th sort class="is-size-6" @click="Sort($event)">State</vs-th>
							<vs-th sort class="is-size-6" @click="Sort($event)">Date</vs-th>
							<vs-th sort class="is-size-6" @click="Sort($event)">Pangolin</vs-th>
							<vs-th sort class="is-size-6" @click="Sort($event)">Nextclade lineage</vs-th>
							<vs-th sort class="is-size-6" @click="Sort($event)">Nextclade clade</vs-th>
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
		<!-- <DesignCircle /> -->

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
import { map } from 'lodash'
import { mapFields } from 'vuex-map-fields'

export default {
	data: () => ({
		page_loaded: false,
		map_bar_switcher: 'Bar',
		version: {
			pangolin: '4.1.3',
			'pangolin-data': '1.15.1',
			constellations: 'v0.1.10',
			scorpio: '0.3.17',
			usher: '0.5.6',
			gofasta: '0.0.5',
			minimap2: '2.24-r1122',
			faToVcf: '426',
			nextclade: '2.8.0',
		},
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
		ClassSection() {
			return this.$device.isDesktop ? 'section timeline-design' : 'section timeline-design-mobile'
		},
		ClassCircle() {
			return this.$device.isDesktop ? 'top-corner' : 'top-corner-mobile'
		},
		...mapFields([
			'stats',
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
		Sort(Event) {
			console.log(Event, this, this.$vs)
		},
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

<style scoped>
.top-corner {
	top: -65%;
	left: -3%;
	width: 20%;
	z-index: 0;
	position: absolute;
}
.top-corner-mobile {
	top: -50%;
	left: -30%;
	width: 100%;
	z-index: 0;
	opacity: 0.1;
	position: absolute;
}
.z-1 {
	z-index: 1;
}
.z-2 {
	z-index: 2;
}
.z-3 {
	z-index: 3;
}
.z-4 {
	z-index: 4;
}
.z-5 {
	z-index: 5;
}
.z-6 {
	z-index: 6;
}
</style>
