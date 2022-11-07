import { ToastProgrammatic as Toast } from 'buefy'
import { getField, updateField } from 'vuex-map-fields'

export const state = () => ({
	total_pages: 1,
	table_data: [],
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
		state_graph_loaded: false,
		seq_week_graph_loaded: false,
	},
})

export const getters = {
	getField,
}

export const mutations = {
	updateField,
	SET_TABLE(state, payload) {
		state.table_data = payload
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
}

export const actions = {
	async nuxtServerInit({ commit, dispatch }, { app, store }) {},
	async GetTable({ commit, dispatch }) {
		try {
			const response = await this.$axios.$post('/query/')
			await commit('SET_TABLE', response.data)
			await commit('SET_PAGES', response.length)
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
}
