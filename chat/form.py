from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
from django import forms
from .models import *


User = get_user_model()

class Registration(UserCreationForm):
     class Meta:
        model = User
        fields = ("username",)
        field_classes = {"username": UsernameField}

class CreateChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = "__all__"

class SendMsgForm(forms.ModelForm):
    class Meta:
        model = ChatMsg
        fields = "__all__"