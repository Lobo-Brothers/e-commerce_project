from django.shortcuts import render

# Create your views here.
from products.models import Product

def home_view(request):
    product = Product.objects.all()
    context = {
        'product': product
    }
    return render(request, "pages/home.html", context)
