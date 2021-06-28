<template>
	<base-template>
		<template #page>
			<router-view></router-view>
		</template>
	</base-template>
</template>
<script>
	import BaseTemplate from './components/base/baseTemplate.vue';

	export default{
		name: "CROOMS",
		components:{
			BaseTemplate
		}
	};
</script>