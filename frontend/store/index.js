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
		deletion: [],
		pangolineage: [],
		substitution: [],
		nextcladelineage: [],
	},
	graphs: {
		state: [],
		state_graph_loaded: false,
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
}
