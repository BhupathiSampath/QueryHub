import { ToastProgrammatic as Toast } from 'buefy'
import { getField, updateField } from 'vuex-map-fields'

export const state = () => ({
	state_name: [],
	deletion_name: [],
	nextclade_name: [],
	pangolineage_name: [],
	substitution_name: [],
	nextcladelineage_name: [],
})

export const getters = {
	getField,
}

export const mutations = {
	updateField,
	SET_STATE_NAME(state, payload) {
		state.state_name = payload
	},
	SET_PANGOLINEAGE_NAME(state, payload) {
		state.pangolineage_name = payload
	},
	SET_NEXTCLADELINEAGE_NAME(state, payload) {
		state.nextcladelineage_name = payload
	},
	SET_NEXTCLADE_NAME(state, payload) {
		state.clade_name = payload
	},
	SET_SUBSTITUTION_NAME(state, payload) {
		state.substitution_name = payload
	},
	SET_DELETION_NAME(state, payload) {
		state.deletion_name = payload
	},
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
	async GetPangolineageNames({ commit, dispatch }) {
		try {
			const response = await this.$axios.$post('/autocomplete/pangolineage/')
			await commit('SET_PANGOLINEAGE_NAME', response)
		} catch (err) {
			Toast.open({
				message: 'err',
				type: 'is-danger',
				position: 'is-top-right',
			})
		}
	},
	async GetNextcladelineageNames({ commit, dispatch }) {
		try {
			const response = await this.$axios.$post('/autocomplete/nextcladelineage/')
			await commit('SET_NEXTCLADELINEAGE_NAME', response)
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
			const response = await this.$axios.$post('/autocomplete/nextclade/')
			await commit('SET_NEXTCLADE_NAME', response)
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
