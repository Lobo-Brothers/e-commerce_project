from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.query_utils import select_related_descend
from django_countries.fields import CountryField    
from .choices import TOP_SIZES

class Profile(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE)
    name            = models.CharField(max_length=64, null=True, blank=True)
    top_sizes       = models.CharField(null=True, blank=True, max_length=3, choices=TOP_SIZES)
    shoes_sizes     = models.PositiveIntegerField(null=True, blank=True, validators=[MinValueValidator(17), MaxValueValidator(48)])
    date_created    = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}, {self.name}'

class Billaddress(models.Model):
    user                = models.CharField(max_length=128)
    name_and_last_name  = models.CharField(max_length=128)
    postal_code         = models.CharField(max_length=64)
    country             = CountryField()
    city                = models.CharField(max_length=64)
    address             = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self):
        return f'{self.user}, {self.name_and_last_name}'