from django.urls import re_path
from .consumers import *

websocket_urlpatterns = [
	# w => is the word and says ROOM_NAME value can be any word wich contains letters,digits,etc
	# $ sign is basically say the paths like ws/chat/roomname/x is not for this consumer
	re_path(r"ws/chat/(?P<room_name>\w+)/$", ChatRoomConsumer.as_asgi()),
]