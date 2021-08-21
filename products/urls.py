from django.urls import path

from .views import *

urlpatterns  =   [
    path('sell/', product_create_view, name='create_product_page')
]