from django.shortcuts import render

# Create your views here.
from .forms import ProfileForm, BillingForm
from .models import Billaddress, Profile

def profile_edit_view(request):
    my_form = ProfileForm(request.POST, user=request.user)

    if request.method == 'POST':
        if my_form.is_valid():
            Profile.object.create(**my_form.cleaned_data)

    context = {
        'form': my_form
    }
    
    return render(request, 'profiles/profile_edit.html', context)

def billing_address_view(request):
    my_form = BillingForm()

    if request.method == 'POST':
        my_form = BillingForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Billaddress.objects.create(**my_form.cleaned_data, belongs_to=request.user.username)

    context = {
        'form': my_form
    }

    return render(request, 'profiles/billing_address_edit.html', context)