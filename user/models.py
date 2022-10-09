from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserCreation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.username