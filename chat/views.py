from django.shortcuts import render, get_object_or_404
from .models import *


def home(request):
    return render(request, "base.html")

def chat(request, slug):
    chat = get_object_or_404(Chat, slug)
    return render(request, "pages/chat.html", {"chat":chat})