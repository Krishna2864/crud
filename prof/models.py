from django.db import models
from  django.contrib.auth.models import  User
from  django.forms import ModelForm

# Create your models here.

#create title

class Title(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return  str(self.title)
    
# create name , description , time

class Userpro(models.Model):
    name = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    description = models.TextField(max_length=250)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)



