from django.shortcuts import render

from .forms import RegisterUserForm

from django.shortcuts import redirect

from django.contrib import messages

#Login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

# Create your views here.

def user_registration_view(request):
    form = RegisterUserForm(request.POST)

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created :)')
            return redirect('/login/')
        else:
            messages.error(request, 'Error, please check that all fields are correct.')
            return redirect('/register')

    context = {'form': form}
    return render(request, 'accounts/user_registration.html', context)

def login_view(request):
    my_form    = AuthenticationForm(request.POST)

    if request.method == 'POST':
        my_form    = AuthenticationForm(request, request.POST)

        if my_form.is_valid():
            username    = my_form.cleaned_data.get('username')
            password    = my_form.cleaned_data.get('password')
            user        = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, 'Succesfully logged in')
                return redirect('/')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'pelotudo de mierda pusiste algo mal')

    context = {'form': my_form}
    return render(request, 'accounts/login.html', context)