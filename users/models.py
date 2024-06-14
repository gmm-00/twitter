from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    profile=models.OneToOneField(User , on_delete=models.CASCADE)
    role=models.CharField(max_length=30,blank=True,default='User')
    image=models.ImageField(default='default.jpg' , upload_to='profile_pic')

    def __str__(self):
        return self.profile.username