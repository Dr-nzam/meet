from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):
    
    first_name = models.CharField(max_length=150, default="")
    last_name = models.CharField(max_length=150, default="")
    username = models.CharField(max_length=150, default="", blank=True)
    email = models.EmailField(unique=True)
    centreInteret = models.CharField(max_length=200, default='',blank=True)
    city = models.CharField(max_length=30, default="")    
    
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    
    def __str__(self):
        return self.email