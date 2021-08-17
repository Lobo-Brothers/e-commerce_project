from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django_countries.fields import CountryField    
from .choices import TOP_SIZES

class Profile(models.Model):
    user                = models.OneToOneField(User, on_delete=models.CASCADE)
    name_and_last_name  = models.CharField(max_length=48, null=True)
    top_sizes           = models.CharField(null=True, max_length=3, choices=TOP_SIZES)
    shoes_sizes         = models.PositiveIntegerField(null=True, validators=[MinValueValidator(17), MaxValueValidator(48)])
    date_created        = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}, {self.name}'

class Billaddress(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    postal_code         = models.CharField(max_length=16)
    country             = CountryField()
    city                = models.CharField(max_length=64)
    address             = models.CharField(max_length=64, null=True)

    def __str__(self):
        return f'{self.address}, {self.city}, {self.postal_code}'