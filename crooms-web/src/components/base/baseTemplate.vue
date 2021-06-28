<template>
	<div class="main">
		<!-- navbar -->
		<base-navbar></base-navbar>

		<!-- main -->
		<main>
			<slot name="page"></slot>
		</main>

		<br>
		<br>
		<br>
		<br>
		<br>
		<br>

		<!-- footer -->
		<baseFooter/>
	</div>
</template>
<script>
	import baseNavbar from '../navbar/baseNavbar.vue';
	import baseFooter from '../footer/baseFooter.vue';

	export default{
		name: "BaseTemplate",
		components:{
			baseNavbar,
			baseFooter
		}
	};
</script>