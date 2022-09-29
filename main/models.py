from email.policy import default
from django.db import models
from django.contrib.auth. models import User
from datetime import date, datetime
# Create your models here.
class post (models.Model):
    author=models.CharField(max_length=20) 
    title=models.CharField(max_length=50, null=True)
    title_tags=models.CharField(max_length=100, null=False, default='tags')
    body=models.TextField(max_length=10000) 
    post_date= models.DateField(auto_now_add=True)
    email=models.CharField(max_length=100, default='email')
    phoneno=models.CharField(max_length=13, default='phone number',null=True)

    
    


    def __str__(self):
        return f'{self.author} post'


class profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg', blank=True)
    phone_number=models.CharField(max_length=12)
    bio=models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return f'{self.user.username} profile'