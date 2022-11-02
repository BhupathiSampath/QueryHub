import { ToastProgrammatic as Toast } from 'buefy'
import { getField, updateField } from 'vuex-map-fields'

export const state = () => ({
	state_name: { raw: [], filtered: [] },
	clade_name: [],
	lineage_name: [],
	deletion_name: [],
	substitution_name: [],
})

export const getters = {
	getField,
}

export const mutations = {
	updateField,
	SET_STATE_NAME(state, payload) {
		state.state_name.raw = payload
		state.state_name.filtered = payload
	},
	SET_LINEAGE_NAME(state, payload) {
		state.lineage_name = payload
	},
	SET_CLADE_NAME(state, payload) {
		state.clade_name = payload
	},
	SET_SUBSTITUTION_NAME(state, payload) {
		state.substitution_name = payload
	},
	SET_DELETION_NAME(state, payload) {
		state.deletion_name = payload
	},
	// SET_SAMPLE_INFO(state, payload) {
	//     state.sample_info = payload
	//     state.sample_loaded = true
	// },
}

export const actions = {
	async GetStateNames({ commit, dispatch }) {
		try {
			const response = await this.$axios.$post('/autocomplete/state/')
			await commit('SET_STATE_NAME', response)
		} catch (err) {
			Toast.open({
				message: 'err',
				type: 'is-danger',
				position: 'is-top-right',
			})
		}
	},
	async GetLineageNames({ commit, dispatch }) {
		try {
			const response = await this.$axios.$post('/autocomplete/lineage/')
			await commit('SET_LINEAGE_NAME', response)
		} catch (err) {
			Toast.open({
				message: 'err',
				type: 'is-danger',
				position: 'is-top-right',
			})
		}
	},
	async GetCladeNames({ commit, dispatch }) {
		try {
			const response = await this.$axios.$post('/autocomplete/clade/')
			await commit('SET_CLADE_NAME', response)
		} catch (err) {
			Toast.open({
				message: 'err',
				type: 'is-danger',
				position: 'is-top-right',
			})
		}
	},
	async GetSubstitutionNames({ commit, dispatch }) {
		try {
			const response = await this.$axios.$post('/autocomplete/substitution/')
			await commit('SET_SUBSTITUTION_NAME', response)
		} catch (err) {
			Toast.open({
				message: 'err',
				type: 'is-danger',
				position: 'is-top-right',
			})
		}
	},
	async GetDeletionNames({ commit, dispatch }) {
		try {
			const response = await this.$axios.$post('/autocomplete/deletion/')
			await commit('SET_DELETION_NAME', response)
		} catch (err) {
			Toast.open({
				message: 'err',
				type: 'is-danger',
				position: 'is-top-right',
			})
		}
	},
}
