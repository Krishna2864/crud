
from django.db import models
from  django.contrib.auth.models import  User
from  django.forms import ModelForm
from  .models import Userpro


class Pro(ModelForm):
    class Meta:
        model = Userpro
        fields = '__all__'