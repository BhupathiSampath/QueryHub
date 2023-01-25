<template>
	<b-navbar :mobile-burger="false" centered class="footer pb-6" shadow type="is-light">
		<template #start>
			<footer>
				<p align="center">
					© 2023 All Rights Reserved<br />
					INSACOG DataHub is developed & maintained by NSM group National Institute of Biomedical
					Genomics (NIBMG), Kalyani <br />
					Source Code is available at
					<a href="https://github.com/animesh-workplace/QueryHub">
						https://github.com/animesh-workplace/QueryHub
					</a>
				</p>
			</footer>
		</template>
	</b-navbar>
</template>

<script>
export default {
	data: () => ({}),
	components: {},
	methods: {},
	mounted() {
		this.$nextTick(() => {})
	},
}
</script>

<style scoped></style>
