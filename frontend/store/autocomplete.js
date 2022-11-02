import { getField, updateField } from 'vuex-map-fields'

export const state = () => ({})

export const getters = {
	getField,
}

export const mutations = {
	updateField,
	// SET_DATA_SUMMARY(state, payload) {
	//     state.data_summary = payload
	// },
	// SET_SAMPLE_INFO(state, payload) {
	//     state.sample_info = payload
	//     state.sample_loaded = true
	// },
}

export const actions = {
	// async GetDataAll({ commit, dispatch }) {
	//     try {
	//         const response = await this.$axios.$post('/data/all/')
	//         await commit('SET_DATA_SUMMARY', response.data)
	//     } catch (err) {
	//         this.$notification.show(err.response.statusText, Object.values(err.response.data)[0], 'ERROR')
	//     }
	// },
}
