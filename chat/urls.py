from django.urls import path
from .views import *

app_name = "chat"

urlpatterns = [
    path("", home, name="home"),
    path("c/<slug:slug>/", ChatView, name="chat"),
    path("chat-msg/", ChatMsgApiView, name="chat_msg")
]
