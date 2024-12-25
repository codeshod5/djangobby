from django.urls import path
from . import consumer
websocket_urls = [
    path('ws/up/',consumer.AreasUpdateConsumer.as_asgi()),
    path('ws/ma/',consumer.MapUpdate.as_asgi())
    
]