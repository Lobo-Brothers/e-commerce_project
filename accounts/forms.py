from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterUserForm(UserCreationForm):
    class Meta:
        model   = User
        fields  = ['username', 'email', 'password1', 'password2']
    
    username    = forms.CharField(required=True, max_length=32, widget=forms.TextInput(attrs={
            'placeholder': 'Username',
            'class': 'signup-labels',
            'title': 'Enter your usarname.'
        }))
    email       = forms.EmailField(required=True, widget=forms.TextInput(attrs={
            'placeholder': 'your@email.com',
            'class': 'signup-labels',
            'title': 'Enter your email.'
        }))
    password1   = forms.CharField(required=True, max_length=64, widget=forms.PasswordInput(attrs={
            'class': 'signup-labels',
            'title': 'Your password must contain at least 8 characters.'
        }))

    password2   = forms.CharField(required=True, max_length=64, widget=forms.PasswordInput(attrs={
            'class': 'signup-labels',
            'title': 'Enter the same password as before, for verification.'
        }))
