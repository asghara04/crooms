"""
THESE CAN BE SET IN ROUTING IF IT SAYS IN DOCUMENT I THINK IS BETTER TODO THAT WAY!
"""

"""
ASGI config for crooms project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crooms.settings')

# when we get a ws(Web Socket) Request this is how manage it, such as urls.py this is urlpatterns
application = ProtocolTypeRouter({
	# simple http requests
	"http": get_asgi_application(),

	# ws => web socket
	'websocket':AuthMiddlewareStack(
		# just authenticated user can access these urls becouse their in AuthMiddlewareStack
		URLRouter(
			# this is like "include("chat.urls.py") and this contain all patterns in routin.py
			# within websocket_urlpatterns variable
			chat.routing.websocket_urlpatterns
		)
	)
})