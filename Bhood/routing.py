from django.urls import path
from .consumers import *
ws_urlpatterns = [
    path('ws/chat/<cname>', Chat.as_asgi()),
]