from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomeUser(AbstractUser):
    is_organiser = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)

