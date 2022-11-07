<template>
	<div>
		<div class="has-text-centered is-size-5 has-text-medium has-text-weight-semibold has-text-grey-dark">
			{{ header }}
		</div>
		<v-chart
			class="chart"
			ref="bar-chart"
			:loading="false"
			:option="options"
			:loading-options="loader_option"
		/>
	</div>
</template>

<script>
import { use } from 'echarts/core'
import { orderBy, map } from 'lodash'
import { BarChart } from 'echarts/charts'
import VChart, { THEME_KEY } from 'vue-echarts'
import { CanvasRenderer } from 'echarts/renderers'
import { GridComponent, LegendComponent, TooltipComponent } from 'echarts/components'

use([BarChart, GridComponent, CanvasRenderer, LegendComponent, TooltipComponent])

export default {
	components: { VChart },
	provide: { [THEME_KEY]: 'light' },
	props: {
		formatter: { type: Function },
		header: { type: String, default: '' },
		chartdata: { type: Array, required: true },
		axislabel: { type: Boolean, default: true },
	},
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
				trigger: 'axis',
				position: 'right',
				borderColor: '#fff',
				axisPointer: { type: 'shadow' },
				textStyle: {
					fontFamily: 'Averta',
					fontWeight: 500,
				},
			},
			series: [],
		},
	}),
	watch: {
		chartdata(value) {
			this.FillChart()
		},
	},
	methods: {
		FillChart() {
			if (this.formatter) {
				this.options.tooltip.formatter = this.formatter
			}

			let output = [
				{
					type: 'bar',
					data: this.$device.isDesktop
						? map(orderBy(this.chartdata, ['label'], 'asc'), (d) => d.value)
						: map(orderBy(this.chartdata, ['label'], 'desc'), (d) => d.value),
					itemStyle: {
						borderRadius: this.$device.isDesktop ? [3, 3, 0, 0] : [0, 3, 3, 0],
					},
					label: {
						fontSize: 11,
						fontWeight: 500,
						fontFamily: 'Averta',
						show: this.axislabel,
						position: this.$device.isDesktop ? 'top' : 'right',
					},
				},
			]
			if (this.$device.isDesktop) {
				this.options.grid = {
					left: 5,
					right: '0%',
					bottom: '0%',
					containLabel: true,
				}
				this.options.yAxis = {
					type: 'value',
					axisLabel: {
						fontFamily: 'Averta',
						fontWeight: 500,
					},
				}
				this.options.xAxis = {
					data: [],
					type: 'category',
					axisLabel: {
						fontFamily: 'Averta',
						fontWeight: 500,
					},
					axisTick: {
						alignWithLabel: true,
					},
				}
				this.options.xAxis.data = map(orderBy(this.chartdata, ['label'], 'asc'), (d) => d.label)
			} else {
				this.options.grid = {
					left: 0,
					right: 15,
					bottom: '0%',
					containLabel: true,
				}
				this.options.xAxis = {
					type: 'value',
					axisLabel: {
						fontFamily: 'Averta',
						fontWeight: 500,
					},
				}
				this.options.yAxis = {
					data: [],
					type: 'category',
					axisLabel: {
						fontFamily: 'Averta',
						fontWeight: 500,
					},
					axisTick: {
						alignWithLabel: true,
					},
				}
				this.options.yAxis.data = map(orderBy(this.chartdata, ['label'], 'desc'), (d) => d.label)
			}
			this.options.series = output
		},
	},
	mounted() {
		this.$nextTick(() => {
			this.FillChart()
		})
	},
}
</script>

<style scoped>
.chart {
	height: 400px;
}
/* Mobile Devices */
@media (max-width: 480px) {
	.chart {
		height: 700px;
	}
}
/* Low resolution Tablets and iPads */
@media (min-width: 481px) and (max-width: 767px) {
	.chart {
		height: 700px;
	}
}
/* Tablets iPads (Portrait) */
@media (min-width: 768px) and (max-width: 1024px) {
	.chart {
		height: 700px;
	}
}
</style>
