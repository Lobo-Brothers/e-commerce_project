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
from django.urls import path

from pages.views import home_view
from products.views import product_create_view
from accounts.views import user_registration_view, user_login_view

from django.conf import settings            #Images stuff
from django.conf.urls.static import static  #Images stuff

urlpatterns = [
    path('admin/', admin.site.urls, name='admin_panel'),
    path('', home_view, name='home_page'),
    path('sell/', product_create_view, name='create_product'),
    path('register/', user_registration_view, name='registration'),
    path('login/', user_login_view, name='login')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)