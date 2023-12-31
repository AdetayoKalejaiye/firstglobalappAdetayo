"""
ASGI config for firstglobalapp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application # for the asgi application
from django.urls import path   # provide the url path 
from chat.consumers import * # it is used for the applications views

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websocket.settings')

application = get_asgi_application()

ws_patterns= [
        
    path('ws/chat/',ChatConsumer.as_asgi())
]

application= ProtocolTypeRouter({

    'websocket' : URLRouter(ws_patterns)


})