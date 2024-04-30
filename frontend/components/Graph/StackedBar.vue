<template>
	<div>
		<p align="center" class="title is-5 has-text-centered has-text-grey-light pt-3">
			VOCs/VOIs/VUIs timeline (past 5 months)
		</p>

		<v-chart
			class="chart"
			:option="options"
			:loading="chart_loader"
			ref="stacked-bar-chart"
			:loading-options="loader_option"
		/>
	</div>
</template>

<script>
import { map } from 'lodash'
import {
	GridComponent,
	TitleComponent,
	LegendComponent,
	ToolboxComponent,
	TooltipComponent,
} from 'echarts/components'
import { use } from 'echarts/core'
import { LineChart, BarChart } from 'echarts/charts'
import VChart, { THEME_KEY } from 'vue-echarts'
import { CanvasRenderer } from 'echarts/renderers'

use([
	BarChart,
	LineChart,
	GridComponent,
	TitleComponent,
	CanvasRenderer,
	LegendComponent,
	ToolboxComponent,
	TooltipComponent,
])

export default {
	data: () => ({
		chart_loader: true,
		loader_option: {
			lineWidth: 3,
			fontSize: 14,
			text: 'Loading',
			fontWeight: 500,
			color: '#c23531',
			maskColor: '#f6f8f9',
			fontFamily: 'Averta',
		},
		options: {
			tooltip: {
				trigger: 'axis',
				borderColor: '#fff',
				transitionDuration: 0.1,
				axisPointer: {
					type: 'line',
					label: {
						show: false,
					},
				},
				textStyle: {
					fontFamily: 'Averta',
					fontWeight: 500,
				},
			},
			legend: {
				top: 'top',
				itemGap: 25,
				itemWidth: 20,
				left: 'center',
				icon: 'roundRect',
				itemHeight: 20,
				textStyle: {
					fontSize: 15,
					fontWeight: 500,
					fontFamily: 'Averta',
				},
				data: [],
			},
			grid: {
				bottom: '10%',
				containLabel: true,
			},
			xAxis: {
				type: 'category',
				axisLabel: {
					fontSize: 12,
					fontWeight: 500,
					fontFamily: 'Averta',
				},
				axisTick: {
					alignWithLabel: true,
				},
				data: [],
			},
			yAxis: {
				max: 100,
				type: 'value',
				axisLabel: {
					fontSize: 12,
					fontWeight: 500,
					fontFamily: 'Averta',
				},
			},
			series: [],
			color: [
				'#fb7293',
				'#37A2DA',
				'#fcd5cf',
				'#f5e8c8',
				'#b8d2c7',
				'#a4d8c2',
				'#f3d999',
				'#d3758f',
				'#c1d7a8',
				'#2e4783',
				'#C4D9E0',
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
		chartdata: { type: Array, required: true },
	},
	methods: {
		async SetChart() {
			let my_data = this.chartdata
			let only_name = map(my_data, (d) => d.name)
			let s = map(my_data, (d) => ({
				stack: true,
				type: 'bar',
				name: d.name,
				data: d.value,
			}))
			this.options.series = s
			this.options.legend.data = only_name
			this.options.xAxis.data = ['Nov-2023', 'Dec-2023', 'Jan-2024', 'Feb-2024', 'Mar-2024']
			if (this.$device.isMobileOrTablet) {
				this.options.grid.y = '30%'
			}
			this.chart_loader = false
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
	height: 300px;
}
.medium {
	height: 600px;
}
.dropdown-content {
	height: 15em;
	overflow: auto;
}
</style>
