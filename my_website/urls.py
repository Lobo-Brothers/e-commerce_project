"""my_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from pages.views import home_view
from products.views import product_create_view

from accounts.views import user_registration_view
from django.contrib.auth import views as auth_views

from profiles.views import profile_edit_view, billing_address_view

from django.conf import settings            #Images stuff
from django.conf.urls.static import static  #Images stuff

urlpatterns = [
    path('admin/', admin.site.urls, name='admin_panel_page'),
    path('', home_view, name='home_page'),
    path('sell/', product_create_view, name='create_product_page'),

    # Accounts app
    path('register/', user_registration_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),

    # Profiles app
    path('profile/edit/', profile_edit_view, name='profile_edit'),
    path('profile/billing', billing_address_view, name='billing_edit')
]

'''Podemos hacer referencia a una url en especifico en el archivo html con {% url 'name' %} , siendo
name el "name" correspondiente al link al que queremos redirigir'''

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)