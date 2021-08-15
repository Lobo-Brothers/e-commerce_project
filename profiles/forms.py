from .models import BillingAddress
from django import forms
from django_countries.fields import CountryField

from django.core.validators import MaxValueValidator, MinValueValidator

from .choices import TOP_SIZES

class ProfileForm(forms.Form):
    name            = forms.CharField(max_length=64)
    #billing_address = forms.ChoiceField(choices = BillingAddress())
    top_sizes       = forms.ChoiceField(choices = TOP_SIZES)
    shoes_sizes     = forms.IntegerField(validators=[MinValueValidator(17), MaxValueValidator(48)])

class BillingForm(forms.Form):
    name_and_last_name  = forms.CharField(max_length=128)
    postal_code         = forms.CharField(max_length=64)
    country             = CountryField().formfield()
    city                = forms.CharField(max_length=64)
    address             = forms.CharField(max_length=64)