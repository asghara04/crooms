<template>
	<!-- header -->
	<header class="p-5 text-center bg-light">
		<h1 class="mb-3">{{this.$route.params.room_name}}</h1>
		<h4 v-if="username">hey <strong>{{username}}</strong> have fun in <strong>{{this.$route.params.room_name}}</strong> chat room :)</h4>
	</header>


	<!-- message section -->
	<section class="row d-flex justify-content-center p-f-centerize-f">
		<div class="col-10">
			
			<!-- chat box -->
			<div class="card">
				<div class="card-body" id="ChatBox" ref="chatBox">
					<!-- messages display here -->
					<p class="text-center"><i><b>{{this.$route.params.room_name}} messages</b></i></p><br>
				</div>
			</div>
			
			<br><br>
			<!-- send message -->
			<form @submit.prevent="sendMessage()">
				<div class="form-group">
					<label for="message">Message:</label>
					<input type="text" name="message" id="message" required="" ref="messageInput" class="form-control">
				</div>
				<br>
				<button class="btn btn-primary btn-block btn-lg">SEND</button>
			</form>
		</div>
	</section>
</template>

<script>
	import API_URL from '@/config.js';
	import {ref,onMounted} from 'vue';
	import {useRoute} from 'vue-router';

	export default{
		name: "ChatRoom",
		setup(){
			const route = useRoute();
			const chatBox = ref(null);
			const messageInput = ref(null);

			const username = ref(null);

			function get_name(){
				username.value = prompt("user name:","");
			}
			get_name();

			// SET WS(webSocket connection)
			const chatSocket = new WebSocket(`ws://${API_URL}/ws/chat/${route.params.room_name}/`)

			chatSocket.onmessage = (e) => {
				console.log(e.data)
				const data = JSON.parse(e.data);
				chatBox.value.innerHTML += `<b>${data['username'] ? data["username"]:"@-ANONYMUOSE"}:</b> ${data['message']}<br>`
			}

			function sendMessage(){
				const message = messageInput.value.value;

				console.log(message)

				if(message){
					chatSocket.send(JSON.stringify({
						"message": message,
						"username": username.value
					}));
				}

				messageInput.value.value = "";
			}

			onMounted(()=>{
				messageInput.value.focus();
			})

			return{
				chatBox,
				messageInput,
				username,
				sendMessage
			}
		}
	};
</script>