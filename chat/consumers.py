from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatRoomConsumer(AsyncWebsocketConsumer):
	async def connect(self):
		# rname => Room Name | LIKE THE uname => username IN LINUX :)
		self.rname = self.scope["url_route"]["kwargs"]["room_name"]
		
		# rgname => Room Group Name
		self.rgname = '%s_Chat' % self.rname

		# Group Layer and AWAITs
		await self.channel_layer.group_add(
			self.rgname,

			# channel name is unique reacher to consumer, I THINK SO! (NOt SURE)
			self.channel_name
		)

		# ACCEPT or REJECT the socket connection between SERVER and CLIENT
		await self.accept()




	async def disconnect(self, close_code):
		await self.channel_layer.group_discard(
			# Group Name to Discard
			self.rgname,
			self.channel_name
		)

	async def receive(self, text_data):
		# get hard usabele text base data from front-end and load it in json format and using it
		text_data_json = json.loads(text_data)
		message = text_data_json["message"]

		# uname => username => i just changing these names for fun :))
		uname = text_data_json["username"]

		await self.channel_layer.group_send(
			self.rgname,
			{
				"type": "croom_message",
				'message': message,
				"username": uname
			}
		)

	async def croom_message(self, event):
		message = event["message"]

		# uname is still stands for username😂 LINE:38
		uname = event["username"]

		await self.send(
			text_data=json.dumps({
				"message": message,
				"username": uname
			})
		)