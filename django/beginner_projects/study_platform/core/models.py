from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    bio=models.TextField(blank=True,null=True)
    profile_pic=models.ImageField(upload_to='profile_pics/',blank=True,null=True)
    goal=models.CharField(max_length=255,blank=True,null=True)
