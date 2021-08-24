from django.shortcuts import render

# Create your views here.
from products.models import Product
from products.models import Category
from random import randint

def home_view(request):
    product = Product.objects.all()
    context = {
        'product': product
    }
    return render(request, "pages/home.html", context)
