<template>
	<div>
		<p align="center" class="is-size-4 has-text-weight-semibold has-text-grey-dark pb-4">
			Monthly Mutation View
		</p>

		<v-chart
			ref="box-chart"
			:option="options"
			class="chart-desktop"
			:loading="chart_loader"
			:loading-options="loader_option"
		/>
	</div>
</template>

<script>
import { use } from 'echarts/core'
import {
	DatasetComponent,
	TitleComponent,
	TooltipComponent,
	GridComponent,
	TransformComponent,
} from 'echarts/components'
import { BoxplotChart, ScatterChart } from 'echarts/charts'
import VChart, { THEME_KEY } from 'vue-echarts'
import { UniversalTransition } from 'echarts/features'
import { CanvasRenderer } from 'echarts/renderers'

use([
	BoxplotChart,
	ScatterChart,
	GridComponent,
	TitleComponent,
	CanvasRenderer,
	DatasetComponent,
	TooltipComponent,
	TransformComponent,
	UniversalTransition,
])
export default {
	data: () => ({
		chart_loader: false,
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
			dataset: [
				{
					// prettier-ignore
					source: [
                [850, 740, 900, 1070, 930, 850, 950, 980, 980, 880, 1000, 980, 930, 650, 760, 810, 1000, 1000, 960, 960, 21],
                [960, 940, 960, 940, 880, 800, 850, 880, 900, 840, 830, 790, 810, 880, 880, 830, 800, 790, 760, 800],
                [880, 880, 880, 860, 720, 720, 620, 860, 970, 950, 880, 910, 850, 870, 840, 840, 850, 840, 840, 840],
                [890, 810, 810, 820, 800, 770, 760, 740, 750, 760, 910, 920, 890, 860, 880, 720, 840, 850, 850, 780],
                [890, 840, 780, 810, 760, 810, 790, 810, 820, 850, 870, 870, 810, 740, 810, 940, 950, 800, 810, 870]
            ],
				},
				{
					transform: {
						type: 'boxplot',
						config: { itemNameFormatter: 'dataset {value}' },
					},
				},
				{
					fromDatasetIndex: 1,
					fromTransformResult: 1,
				},
			],
			tooltip: {
				trigger: 'item',
				axisPointer: {
					type: 'shadow',
				},
			},
			grid: {
				left: '10%',
				right: '10%',
				bottom: '15%',
			},
			xAxis: {
				type: 'category',
				splitArea: { show: false },
				splitLine: { show: false },
			},
			yAxis: {
				type: 'value',
				splitArea: { show: false },
			},
			series: [
				{
					name: 'boxplot',
					type: 'boxplot',
					datasetIndex: 1,
				},
				{
					name: 'outlier',
					type: 'scatter',
					datasetIndex: 2,
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
		ChartData: { type: Array },
	},
	methods: {},
	mounted() {
		this.$nextTick(() => {})
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
