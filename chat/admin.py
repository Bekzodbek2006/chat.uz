from django.contrib import admin
from .models import *

admin.site.register(CustomeUser)
admin.site.register(Chat)
admin.site.register(ChatMsg)
