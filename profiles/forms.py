from django import forms
from django.forms.widgets import Select
from django_countries.fields import CountryField

from django.core.validators import MaxValueValidator, MinValueValidator

from .choices import TOP_SIZES
from .models import Billaddress, Profile

class ProfileForm(forms.Form):

    class Meta:
        model   = Profile
        fields  = ['address']

    def __init__(self, *args, **kwargs):
        self.username    =   kwargs.pop("user")
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['address'] = forms.ModelMultipleChoiceField(queryset=Billaddress.objects.filter(user = self.username), widget=Select)

    name            = forms.CharField(max_length=64)
    top_sizes       = forms.ChoiceField(choices = TOP_SIZES)
    shoes_sizes     = forms.IntegerField(validators=[MinValueValidator(17), MaxValueValidator(48)])

class BillingForm(forms.Form):
    name_and_last_name  = forms.CharField(max_length=128)
    postal_code         = forms.CharField(max_length=64)
    country             = CountryField().formfield()
    city                = forms.CharField(max_length=64)
    address             = forms.CharField(max_length=64)