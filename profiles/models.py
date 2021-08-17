from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django_countries.fields import CountryField    


class Profile(models.Model):
    user                = models.OneToOneField(User, on_delete=models.CASCADE)
    name_and_last_name  = models.CharField(default='', blank=True, max_length=48)
    date_created        = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'

class Billaddress(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    postal_code         = models.CharField(max_length=16, blank=True)
    country             = CountryField()
    city                = models.CharField(max_length=64, blank=True)
    address             = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return f'{self.address}, {self.city}, {self.postal_code}'