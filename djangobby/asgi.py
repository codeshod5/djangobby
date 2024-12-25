"""
ASGI config for djangobby project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
import accou.routing
from channels.auth import AuthMiddlewareStack
import buses.routing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangobby.settings')




application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':URLRouter(
        buses.routing.websocket_urls
    )
})