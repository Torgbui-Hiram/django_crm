from django import forms
from django.contrib.auth import models
from django.contrib.auth.admin import UserCreationForm
from member.models import CustomUser


class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
