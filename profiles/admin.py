from django.contrib import admin

# Register your models here.

from .models import Profile, Billaddress

admin.site.register(Profile)
admin.site.register(Billaddress)