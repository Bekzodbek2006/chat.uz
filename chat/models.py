from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomeUser(AbstractUser):
    is_organiser = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)



class Chat(models.Model):
    author = models.ForeignKey(CustomeUser, on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    img = models.ImageField(blank=True)
    file = models.FileField(blank=True)

    def __str__(self):
        return f"id: {self.pk} message: {self.message}"