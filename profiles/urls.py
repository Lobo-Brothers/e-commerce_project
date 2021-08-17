from django.urls import path

from .views import *

urlpatterns  =   [
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', profile_edit_view, name='profile_edit'),
    path('profile/billing', billing_address_view, name='billing_edit')
]