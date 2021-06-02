from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    phone_number = models.CharField(max_length=11)
    address = models.CharField(max_length=150)
    point = models.TextField(default=0)
    ranking = models.TextField(default="WELCOME")
