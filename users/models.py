from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    fullName = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    age = models.DateField()
    address = models.TextField(max_length=50)
    phone = models.CharField(max_length=15, unique=True)
    
def __str__(self):
    return self.username
    
    
