from django.contrib import admin

# Register your models here.

from .models import Product, Category
from mptt.admin import MPTTModelAdmin

admin.site.register(Product)
admin.site.register(Category, MPTTModelAdmin)
