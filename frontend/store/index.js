import { ToastProgrammatic as Toast } from 'buefy'
import { getField, updateField } from 'vuex-map-fields'

export const state = () => ({
	total_pages: 1,
	table_data: [],
	stats: {},
	filters: {
		page: 1,
		clade: [],
		state: [],
		dates: [],
		search: [],
		deletion: [],
		mode: 'Monthly',
		pangolineage: [],
		substitution: [],
		nextcladelineage: [],
	},
	graphs: {
		state: [],
		seq_week: [],
		substitution: [],
		state_graph_loaded: false,
		substitution_loaded: false,
		seq_week_graph_loaded: false,
	},
	stacked_bar_chart: [
		{ name: 'Omicron', value: [96.21, 97.1, 96.26, 93.18, 91.21] },
		{ name: 'Delta', value: [0.07, 0.04, 0.0, 0.12, 0.0] },
		{ name: 'Unassigned', value: [0.91, 0.66, 1.59, 2.89, 5.49] },
		{ name: 'Recombinant', value: [2.81, 2.21, 2.15, 3.82, 3.3] },
	],
})

export const getters = {
	getField,
}

export const mutations = {
	updateField,
	SET_TABLE(state, payload) {
		state.table_data = payload
	},
	SET_STATS(state, payload) {
		state.stats = payload
	},
	SET_PAGES(state, payload) {
		state.total_pages = payload
	},
	SET_GRAPH_STATE(state, payload) {
		state.graphs.state = payload
		state.graphs.state_graph_loaded = true
	},
	SET_GRAPH_SEQ_WEEK(state, payload) {
		state.graphs.seq_week = payload
		state.graphs.seq_week_graph_loaded = true
	},
	SET_GRAPH_SUBSTITUTION(state, payload) {
		state.graphs.substitution = payload
		state.graphs.substitution_loaded = true
	},
}

export const actions = {
	async nuxtServerInit({ commit, dispatch }, { app, store }) {},
	async GetStats({ commit, dispatch }) {
		try {
			const response = await this.$axios.$post('/stats/')
			await commit('SET_STATS', response)
		} catch (err) {
			Toast.open({
				message: 'err',
				type: 'is-danger',
				position: 'is-top-right',
			})
		}
	},
	async GetTable({ commit, dispatch }) {
		try {
			const response = await this.$axios.$post('/query/')
			await commit('SET_TABLE', response.data)
			await commit('SET_PAGES', response.length)
			await commit('SET_STATS', response.stats)
		} catch (err) {
			Toast.open({
				message: 'err',
				type: 'is-danger',
				position: 'is-top-right',
			})
		}
	},
	async UpdateTable({ commit, dispatch, state }) {
		try {
			const response = await this.$axios.$post('/query/', state.filters)
			await commit('SET_TABLE', response.data)
			await commit('SET_PAGES', response.length)
			await commit('SET_STATS', response.stats)
		} catch (err) {
			Toast.open({
				message: 'err',
				type: 'is-danger',
				position: 'is-top-right',
			})
		}
	},
	async GetStateGraph({ commit, dispatch, state }) {
		try {
			const response = await this.$axios.$post('/graph/state-count/', state.filters)
			await commit('SET_GRAPH_STATE', response)
		} catch (err) {
			Toast.open({
				message: 'err',
				type: 'is-danger',
				position: 'is-top-right',
			})
		}
	},
	async GetSequenceWeeklyGraph({ commit, dispatch, state }) {
		try {
			const response = await this.$axios.$post('/graph/sequence-count/', state.filters)
			await commit('SET_GRAPH_SEQ_WEEK', response)
		} catch (err) {
			Toast.open({
				message: 'err',
				type: 'is-danger',
				position: 'is-top-right',
			})
		}
	},
	async GetSubstitutionGraph({ commit, dispatch, state }) {
		try {
			const response = await this.$axios.$post('/graph/substitution-count/', state.filters)
			await commit('SET_GRAPH_SUBSTITUTION', response)
		} catch (err) {
			Toast.open({
				message: 'err',
				type: 'is-danger',
				position: 'is-top-right',
			})
		}
	},
}
