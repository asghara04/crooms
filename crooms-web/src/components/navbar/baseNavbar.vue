<template>
	<nav class="navbar navbar-expand-lg navbar-dark bg-primary">
		<div class="container-fluid">

			<!-- brand name -->
			<a href="/" class="navbar-brand">
				<img src="@/assets/icon.svg" width="30" height="24" class="d-inline-block align-text-top">
				CROOMS
			</a>

			<!-- toggle -->
			<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
				<span class="navbar-toggler-icon"></span>
			</button>

			<!-- nav options -->
			<div class="collapse navbar-collapse" id="navbarNav">
				<ul class="navbar-nav">
					<li class="nav-item">
						<router-link class="nav-link active" :to="{name: 'About'}">ABOUT CROOMS</router-link>
					</li>
				</ul>
			</div>
		</div>
	</nav>
</template>
<script>
	export default{
		name: "baseNavbar",

	};
</script>