from django.shortcuts import render, get_object_or_404
from .models import *
from .serializers import *

#rest_framework
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, filters, generics

def home(request):
    return render(request, "base.html")

def ChatView(request, slug):
    # chat = get_object_or_404(Chat, slug)
    chat = Chat.objects.get(slug=slug)
    return render(request, "pages/chat.html", {"chat":chat})


### ChatMsg API
# ChatMsg all API
@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def ChatMsgApiView(request):
    chat_msg = ChatMsg.objects.all()
    serializer = ChatMsgApi(chat_msg, many=True)
    return Response(serializer.data)
