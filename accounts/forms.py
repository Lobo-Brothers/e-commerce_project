from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterUserForm(UserCreationForm):
    class Meta:
        model   = User
        fields  = ['username', 'email', 'password1', 'password2']
    
    username    = forms.CharField(required=True, max_length=32, widget=forms.TextInput(attrs={
            'placeholder': 'Username',
            'class': 'signup-labels'
        }))
    email       = forms.EmailField(required=True, widget=forms.TextInput(attrs={
            'placeholder': 'your@email.com',
            'class': 'signup-labels'
        }))
    password1   = forms.CharField(required=True, max_length=64, widget=forms.PasswordInput(attrs={
            'class': 'signup-labels'
        }))

    password2   = forms.CharField(required=True, max_length=64, widget=forms.PasswordInput(attrs={
            'class': 'signup-labels'
        }))
