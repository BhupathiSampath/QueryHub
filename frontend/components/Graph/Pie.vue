<template>
	<div>
		<p align="center" class="is-size-4 has-text-weight-semibold has-text-grey-dark pb-4">Mutation View</p>

		<v-chart
			ref="pie-chart"
			:option="options"
			class="chart-desktop"
			:loading="chart_loader"
			:loading-options="loader_option"
		/>
	</div>
</template>

<script>
import { use } from 'echarts/core'
import { PieChart, LineChart, ScatterChart } from 'echarts/charts'
// import { mapFields } from 'vuex-map-fields'
import VChart, { THEME_KEY } from 'vue-echarts'
import { CanvasRenderer } from 'echarts/renderers'
import { PolarComponent, LegendComponent, TooltipComponent } from 'echarts/components'

use([PieChart, LineChart, CanvasRenderer, LegendComponent, TooltipComponent, PolarComponent, ScatterChart])

export default {
	data: () => ({
		chart_loader: true,
		loader_option: {
			lineWidth: 3,
			fontSize: 14,
			fontWeight: 500,
			text: 'Loading',
			color: '#c23531',
			fontFamily: 'Averta',
			maskColor: '#f6f8f9',
		},
		options: {
			tooltip: {
				trigger: 'item',
				axisPointer: {
					type: 'shadow',
				},
				transitionDuration: 0.1,
				borderColor: '#fff',
				textStyle: {
					fontSize: 15,
					fontWeight: 500,
					fontFamily: 'Averta',
				},
				formatter: function (params) {
					return `<b>${params.name.split(' ')[0]}</b>`
				},
			},
			grid: [
				{
					// Desktop setting
					left: '32%',
					right: '33.5%',
					bottom: '5.8%',
					containLabel: true,

					// Temporary setting
					// top: '1%',
					// left: '20%',
					// right: '20%',
					// bottom: '0%',
					// containLabel: true,

					// Mobile version
					// left: '0%',
					// bottom: '6%',
					// right: '8.5%',
					// containLabel: true,
				},
				{
					left: '3%',
					right: '3%',
					bottom: '5%',
					containLabel: true,
				},
			],
			legend: {
				left: 10,
				itemGap: 18,
				itemWidth: 20,
				type: 'scroll',
				icon: 'circle',
				itemHeight: 15,
				orient: 'vertical',
				padding: [0, 0, 0, 0],
				textStyle: {
					fontSize: 15,
					fontWeight: 500,
					fontFamily: 'Averta',
				},
				// show: false,
				data: [
					{ name: "5'UTR" },
					{ name: 'ORF1a' },
					{ name: 'ORF1b' },
					{ name: 'Spike' },
					{ name: 'ORF3a' },
					{ name: 'Envelope' },
					{ name: 'Membrane' },
					{ name: 'ORF6' },
					{ name: 'ORF7a' },
					{ name: 'ORF7b' },
					{ name: 'ORF8' },
					{ name: 'Nucleocapsid' },
					{ name: 'ORF9b' },
					{ name: "3'UTR" },
				],
			},
			xAxis: {
				show: false,
				min: -10,
				max: 10,
				gridIndex: 0,
			},

			yAxis: {
				show: false,
				min: -10,
				max: 10,
				gridIndex: 0,
			},
			angleAxis: {
				show: false,
				type: 'value',
				max: 29903,
				startAngle: -90,
				splitLine: {
					show: true,
				},
				scale: true,
			},
			radiusAxis: {
				show: false,
				min: 0,
				type: 'value',
				splitLine: {
					show: false,
				},
			},
			polar: {
				radius: '95%',
			},
			series: [
				{
					z: 0,
					data: [],
					// bottom: '1.6%',
					// left: '1.5%',
					type: 'pie',
					startAngle: -90,
					radius: ['65%', '80%'],
					avoidLabelOverlap: true,
					itemStyle: {
						borderWidth: 2,
						borderRadius: 5,
						borderCap: 'round',
						borderJoin: 'bevel',
						borderColor: '#fff',
					},
					label: {
						show: false,
						fontSize: 12,
						fontWeight: 500,
						alignTo: 'edge',
						color: '#9C9090',
						position: 'outside',
						fontFamily: 'Averta',
					},
					labelLine: {
						length: 10,
						length2: 20,
						smooth: 0.2,
						lineStyle: {
							color: '#DFDAD7',
						},
					},
					emphasis: {
						disabled: true,
						// scale: false,
						// focus: 'self',
						// label: { show: true },
					},
					// tooltip: { trigger: 'none' },
				},
				{
					z: 2,
					data: [],
					top: '6.6%',
					type: 'pie',
					bottom: '6.6%',
					cursor: 'normal',
					selectedMode: false,
					label: { show: false },
					itemStyle: { color: '#fff' },
					emphasis: { disabled: true },
					tooltip: { trigger: 'none' },
				},
				{
					z: 1,
					type: 'line',
					symbol: 'none',
					// symbolSize: 10,
					coordinateSystem: 'polar',
					// data: [
					// 	[0, 0],
					// 	[0, 10, 'Mutation1x1'],
					// 	[0, 0],
					// 	[0, -10, 'Mutation1x2'],
					// 	[0, 0],
					// 	[10, 0, 'Mutation1y1'],
					// 	[0, 0],
					// 	[-10, 0, 'Mutation1y2'],
					// 	[0, 0],
					// 	[7.2, 7.2, 'Mutation2'],
					// 	[0, 0],
					// 	[10, 7, 'Mutation3'],
					// 	[0, 0],
					// 	[10, 8, 'Mutation4'],
					// 	[0, 0],
					// 	[-5, 10, 'Mutation5'],
					// ],
					data: [
						[0, 0],
						[100, 1000, 'Mutation1x1'],
						[0, 0],
						[100, 2000, 'Mutation1x2'],
						[0, 0],
						[100, 3000, 'Mutation1y1'],
						[0, 0],
						[100, 4000, 'Mutation1y2'],
						[0, 0],
						[100, 5000, 'Mutation2'],
						[0, 0],
						[100, 6000, 'Mutation3'],
						[0, 0],
						[100, 8000, 'Mutation4'],
						[0, 0],
						[100, 10000, 'Mutation5'],
					],
					label: {
						// show: true,
						fontSize: 12,
						fontWeight: 500,
						align: 'center',
						verticalAlign: 'top',
						// offset: [40, 0],
						color: '#8A7D7F',
						// position: 'outside',
						fontFamily: 'Averta',
						formatter: function (params) {
							return params.value[2] ?? ''
						},
					},
					// labelLine: {
					// 	show: true,
					// 	// showAbove: true,
					// 	length: 10,
					// 	length2: 20,
					// 	// smooth: 0.2,
					// },
					labelLayout: { hideOverlap: true },
					// labelLayout: { moveOverlap: 'shiftY' },
					itemStyle: { color: '#8A7D7F' },
				},
				{
					z: 3,
					type: 'scatter',
					coordinateSystem: 'polar',
					symbol: 'circle',
					itemStyle: {
						opacity: 1,
						color: '#efe111',
					},
					symbolSize: 15,
					data: [
						[100, 1000],
						[100, 1050],
						[100, 2000],
						[100, 3000],
						[100, 4000],
						[100, 5000],
						[100, 6000],
						[100, 8000],
						[100, 10000],
					],
				},

				// {
				// 	z: 1,
				// 	type: 'line',
				// 	data: [
				// 		[0, 0],
				// 		[0, 10, 'Mutation1'],
				// 	],
				// 	endLabel: {
				// 		show: true,
				// 		fontSize: 12,
				// 		fontWeight: 500,
				// 		alignTo: 'edge',
				// 		color: '#8A7D7F',
				// 		position: 'outside',
				// 		fontFamily: 'Averta',
				// 		formatter: function (params) {
				// 			return params.value[2]
				// 		},
				// 	},
				// 	itemStyle: { color: '#8A7D7F' },
				// },
				// {
				// 	z: 1,
				// 	type: 'line',
				// 	data: [
				// 		[0, 0],
				// 		[50, 7000],
				// 	],
				// 	symbolSize: 10,
				// 	coordinateSystem: 'polar',
				// 	endLabel: {
				// 		show: true,
				// 		fontSize: 12,
				// 		fontWeight: 500,
				// 		alignTo: 'edge',
				// 		color: '#8A7D7F',
				// 		position: 'outside',
				// 		fontFamily: 'Averta',
				// 		formatter: function (params) {
				// 			return params.value[2]
				// 		},
				// 	},
				// 	itemStyle: { color: '#8A7D7F' },
				// },
				// {
				// 	z: 1,
				// 	type: 'line',
				// 	data: [
				// 		[0, 0],
				// 		[50, 7500, 'Mutation3'],
				// 	],
				// 	symbolSize: 10,
				// 	coordinateSystem: 'polar',
				// 	endLabel: {
				// 		show: true,
				// 		fontSize: 12,
				// 		fontWeight: 500,
				// 		alignTo: 'edge',
				// 		color: '#8A7D7F',
				// 		position: 'outside',
				// 		fontFamily: 'Averta',
				// 		formatter: function (params) {
				// 			return params.value[2]
				// 		},
				// 	},
				// 	itemStyle: { color: '#8A7D7F' },
				// },
				// {
				// 	z: 1,
				// 	type: 'line',
				// 	data: [
				// 		[0, 0],
				// 		[10, 7.3, 'Mutation5'],
				// 	],
				// 	label: {
				// 		show: true,
				// 		fontSize: 12,
				// 		fontWeight: 500,
				// 		alignTo: 'edge',
				// 		color: '#8A7D7F',
				// 		position: 'outside',
				// 		fontFamily: 'Averta',
				// 		formatter: function (params) {
				// 			return params.value[2]
				// 		},
				// 	},
				// 	itemStyle: { color: '#8A7D7F' },
				// },
				// {
				// 	z: 1,
				// 	type: 'line',
				// 	data: [
				// 		[0, 0],
				// 		[10, 7.5, 'Mutation4'],
				// 	],
				// 	endLabel: {
				// 		show: true,
				// 		fontSize: 12,
				// 		fontWeight: 500,
				// 		alignTo: 'edge',
				// 		color: '#8A7D7F',
				// 		position: 'outside',
				// 		fontFamily: 'Averta',
				// 		formatter: function (params) {
				// 			return params.value[2]
				// 		},
				// 	},
				// 	itemStyle: { color: '#8A7D7F' },
				// },
			],
			color: [
				'#37a2da',
				'#32c5e9',
				'#67e0e3',
				'#9fe6b8',
				'#ffdb5c',
				'#ff9f7f',
				'#fb7293',
				'#e062ae',
				'#e690d1',
				'#e7bcf3',
				'#9d96f5',
				'#8378ea',
				'#96bfff',
			],
		},
	}),
	components: {
		VChart,
	},
	provide: {
		[THEME_KEY]: 'light',
	},
	props: {},
	watch: {},
	computed: {
		// ...mapFields(['landing_info', 'landing_info_loaded']),
	},
	methods: {
		async get_chartdata() {
			// if (this.landing_info_loaded) {
			// this.options.series[0].data = [
			// 	// { name: '', value: 2000 },
			// 	{ name: "5'UTR", value: 50 },
			// 	{ name: 'ORF1a', value: 50 },
			// 	{ name: 'ORF1b', value: 50 },
			// 	{ name: 'Spike', value: 50 },
			// ]
			this.options.series[0].data = [
				// { name: '', value: 2000 },
				{ name: "5'UTR", value: 266 },
				{ name: 'ORF1a', value: 13202 },
				{ name: 'ORF1b', value: 8087 },
				{ name: 'Spike', value: 3821 },
				{ name: 'ORF3a', value: 827 },
				{ name: 'Envelope', value: 227 },
				{ name: 'Membrane', value: 668 },
				{ name: 'ORF6', value: 185 },
				{ name: 'ORF7a', value: 365 },
				{ name: 'ORF7b', value: 131 },
				{ name: 'ORF8', value: 365 },
				{ name: 'Nucleocapsid', value: 1259 },
				{ name: 'ORF9b', value: 293 },
				{ name: "3'UTR", value: 228 },
			]
			this.options.series[1].data = [{ name: 'Donot show', value: 266 }]
			// this.options.series[0].label.formatter = `Total: ${this.landing_info.genomes_sequenced.toLocaleString(
			// 	'en-IN',
			// )}`
			if (this.$device.isMobileOrTablet) {
				this.options.series[0].top = '0%'
				this.options.series[0].radius = ['20%', '100%']
			}
			// }
			this.chart_loader = false
		},
	},
	beforeMount() {},
	mounted() {
		this.$nextTick(() => {
			this.get_chartdata()
		})
	},
}
</script>

<style scoped>
.chart-desktop {
	height: 700px;
}
.chart-mobile {
	height: 800px;
}
</style>
