export default {
	loading: false,
	components: true,
	head: {
		title: 'frontend',
		htmlAttrs: { lang: 'en' },
		meta: [
			{ charset: 'utf-8' },
			{
				name: 'viewport',
				content: 'width=device-width, initial-scale=1',
			},
			{ name: 'format-detection', content: 'telephone=no' },
			{ hid: 'description', name: 'description', content: '' },
		],
		link: [{ rel: 'icon', type: 'image/x-icon', href: `${process.env.ROUTER_BASE}favicon.ico` }],
	},
	plugins: ['@/plugins/plugin-vuesax'],
	axios: { baseURL: process.env.BASE_URL },
	modules: ['@nuxtjs/axios', 'nuxt-buefy'],
	router: { base: process.env.ROUTER_BASE },
	css: ['vuesax/dist/vuesax.css', 'static/css/styles.css'],
	build: {
		transpile: [/echarts/, /zrender/],
		babel: {
			plugins: [
				['@babel/plugin-proposal-optional-chaining', { loose: true }],
				['@babel/plugin-proposal-private-property-in-object', { loose: true }],
				['@babel/plugin-proposal-nullish-coalescing-operator', { loose: true }],
			],
		},
	},
	buildModules: ['@nuxtjs/google-fonts', '@nuxtjs/composition-api/module', '@nuxtjs/device'],
	googleFonts: {
		preload: true,
		prefetch: true,
		download: true,
		display: 'swap',
		preconnect: true,
		overwriting: false,
		families: { 'Lexend Deca': ['100', '200', '300', '400', '500', '600', '700', '800', '900'] },
	},
}
