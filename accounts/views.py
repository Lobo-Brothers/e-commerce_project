from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm

from django.shortcuts import redirect

from django.contrib import messages

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