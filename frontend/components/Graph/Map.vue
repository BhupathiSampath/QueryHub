<template>
	<div>
		<div class="has-text-centered is-size-5 has-text-medium has-text-weight-semibold has-text-grey-dark">
			{{ header }}
		</div>
		<v-chart class="chart" :loading="false" :option="options" :loading-options="loader_option" />
	</div>
</template>

<script>
import {
	GeoComponent,
	TitleComponent,
	ToolboxComponent,
	TooltipComponent,
	VisualMapComponent,
} from 'echarts/components'
import { map, max, ceil } from 'lodash'
import { MapChart } from 'echarts/charts'
import IN from '@/assets/maps/india.json'
import { feature } from 'topojson-client'
import VChart, { THEME_KEY } from 'vue-echarts'
import { use, registerMap } from 'echarts/core'
import { CanvasRenderer } from 'echarts/renderers'

use([
	MapChart,
	GeoComponent,
	CanvasRenderer,
	TitleComponent,
	ToolboxComponent,
	TooltipComponent,
	VisualMapComponent,
])
// RegisterMap needs to come after the use function otherwise doesn't work
registerMap('India', feature(IN, IN.objects.states))

export default {
	data: () => ({
		loader_option: {
			lineWidth: 3,
			fontSize: 14,
			text: 'Loading',
			fontWeight: 500,
			color: '#c23531',
			fontFamily: 'Averta',
		},
		options: {
			tooltip: {
				trigger: 'item',
				position: 'right',
				formatter: '{b}: {c}',
				borderColor: '#fff',
				textStyle: {
					fontSize: 14,
					fontWeight: 500,
					fontFamily: 'Averta',
				},
			},
			visualMap: {
				min: 0,
				max: 10,
				align: 'top',
				orient: 'horizontal',
				inRange: {
					color: [
						'#e6f2fb',
						'#cee5f6',
						'#b5d9f2',
						'#9ccced',
						'#84bfe9',
						'#6bb2e4',
						'#52a5e0',
						'#3999db',
						'#218cd7',
						'#087fd2',
					],
				},
				textStyle: {
					fontSize: 14,
					fontWeight: 500,
					color: '#706266',
					fontFamily: 'Averta',
				},
			},
			series: [
				{
					data: [],
					zoom: 1.14,
					type: 'map',
					map: 'India',
					aspectScale: 0.85,
					nameProperty: 'st_nm',
					itemStyle: { borderColor: '#9C9090' },
					emphasis: {
						label: { show: false },
						itemStyle: {
							borderWidth: 2,
							areaColor: 'inherit',
							borderColor: '#2D232E',
						},
					},
					select: {
						label: { show: false },
						itemStyle: {
							borderWidth: 2,
							areaColor: 'inherit',
							borderColor: '#2D232E',
						},
					},
				},
			],
		},
	}),
	components: {
		VChart,
	},
	provide: {
		[THEME_KEY]: 'light',
	},
	props: {
		header: { type: String, required: true },
		chartdata: { type: Array, required: true },
	},
	watch: {
		chartdata(value) {
			this.SetChart()
		},
	},
	computed: {},
	methods: {
		SetChart() {
			let max_value = ceil(max(map(this.chartdata, (d) => d.value)), -2)
			this.options.series[0].data = this.chartdata
			this.options.visualMap.max = max_value
			this.options.visualMap.text = [max_value, 0]
		},
	},
	mounted() {
		this.$nextTick(() => {
			this.SetChart()
		})
	},
}
</script>

<style scoped>
.chart {
	height: 600px;
}
</style>
