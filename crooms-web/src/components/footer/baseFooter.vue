<template>
<footer class="text-center bg-dark text-white">

	<div class="container p-4">
		<section class="mb-4">
			<a target="_blank" href="https://instagram.com/asghar.a04/" class="btn btn-outline-light btn-floating m-1">
				<i class="fab fa-instagram"></i>
				<BIconInstagram/>
			</a>
			<a target="_blank" href="https://m.youtube.com/channel/UCH7JSiiuMVFLYRrO5n3UchA" class="btn btn-outline-light btn-floating m-1">
				<i class="fab fa-youtube"></i>
				<BIconYoutube/>
			</a>
			<a target="_blank" href="https://github.com/asghara04/" class="btn btn-outline-light btn-floating m-1">
				<i class="fab fa-github"></i>
				<BIconGithub/>
			</a>
		</section>

		<section class="mb-4">
			<h4>SUPPORT</h4>
			<p>Buy Me a Coffee By: </p>
			<p>XRP: rrhXWEwk7wpsdV77Wcb7S3VFRSt7EGGHU4</p>
			Donate Me By XRP Coin💖
		</section>
	</div>

	<div class="text-center p-3" style="background-color: rgba(0,0,0,0.2);">
		By <strong>Asghar Ale</strong>
	</div>
</footer>
</template>
<script>
	import {BIconInstagram, BIconYoutube, BIconGithub} from 'bootstrap-icons-vue';
	export default{
		name: "baseFooter",
		components:{
			BIconInstagram,
			BIconYoutube,
			BIconGithub
		}
	};
</script>