from django.contrib import admin

# Register your models here.

from .models import Profile, BillingAddress

admin.site.register(Profile)
admin.site.register(BillingAddress)