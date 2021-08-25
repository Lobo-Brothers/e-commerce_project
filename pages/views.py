from django.shortcuts import render

# Create your views here.
from products.models import Product

def home_view(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, "pages/home.html", context)
