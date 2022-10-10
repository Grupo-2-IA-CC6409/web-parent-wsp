from asyncore import write
from enum import unique
from msilib.schema import Class
from django.forms import ModelForm
from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, AbstractUser
from .models import CustomUser



class CreateUserForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name','email', 'password1','password2']


