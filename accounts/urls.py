from django.urls import path

from .views import *
from django.contrib.auth import views as auth_views

urlpatterns  =   [
    path('register/', user_registration_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
]