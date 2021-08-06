from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .forms import RegisterUserForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
# Create your views here.

def user_registration_view(request):
    form = RegisterUserForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(user_login_view)
    
    context = {'form': form}
    return render(request, 'registration/user_registration.html', context)

def user_login_view(request):
    form = 'hola'

    context = {'form': form}
    return render(request, 'registration/user_login.html', context)