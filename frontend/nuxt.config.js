export default {
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
		link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
	},
	css: [],
	axios: {},
	plugins: [],
	components: true,
	buildModules: [],
	modules: ['@nuxtjs/axios', ['nuxt-buefy', { materialDesignIcons: false }]],
	build: {
		babel: {
			plugins: [
				['@babel/plugin-proposal-optional-chaining', { loose: true }],
				['@babel/plugin-proposal-private-property-in-object', { loose: true }],
				['@babel/plugin-proposal-nullish-coalescing-operator', { loose: true }],
			],
		},
	},
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
