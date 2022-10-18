from rest_framework import serializers
from .models import *


class ChatMsgApi(serializers.ModelSerializer):
    class Meta:
        model = ChatMsg
        fields = '__all__'