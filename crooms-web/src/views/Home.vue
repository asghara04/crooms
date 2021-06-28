<template>

	<!-- header -->
	<header class="p-5 text-center bg-light">
		<h1 class="mb-3">CROOMS</h1>
		<h4 class="mb-3">free chat rooms for every one!</h4>
	</header>

	<!-- search form -->
	<!-- 
		d => display
		lg => large
		sm => small
		btn => button

		p-f-centerize-f => page fully centerize with flexbos (IN "@/THEME/CORE.CSS")
	-->
	<!-- THIS CAN BE A WHOLE COMPONENT AND ALSO GET USED INTO NAVIGATION BUT THIS IS ENUOGH FOR NOW! -->
	<form class="p-f-centerize-f" @submit.prevent="load_room()">
		<div class="form-group px-2">
			<label for="chatRoomName">Chat Room Name:</label>
			<input type="text" ref="room_name" name="chatRoomName" id="chatRoomName" class="form-control form-control-lg" placeholder="room name..." required="">
		</div>
		<button type="submit" class="btn btn-lg btn-primary">Let's Go :)</button>
	</form>
</template>

<script>
// @ is an alias to /src
import {ref, onMounted} from 'vue';
import {useRouter} from 'vue-router';

export default {
	name: 'Home',
	components: {
	},
	setup(){
		const router = useRouter();
		const room_name = ref(false);

		function load_room(){
			const room = room_name.value.value;

			if(!room){
				alert("enter a room name to continue please.")
			}else{
				router.push({name: "chatRoom", params:{room_name: room}})
			}
		}


		onMounted(()=>{
			document.querySelector("#chatRoomName").focus()
		})


		return{
			room_name,
			load_room
		}
	}
};
</script>
