from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import forms
from django.forms.models import fields_for_model

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model   = User
        fields  = ['username', 'email', 'password1', 'password2']