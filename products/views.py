from django.shortcuts import render

from .forms import ProductForm 
from .models import Product, Category

# Create your views here.

def product_create_view(request):
    my_form = ProductForm(request.POST, request.FILES)
    if request.method == "POST":
        if my_form.is_valid():
            Product.objects.create(**my_form.cleaned_data)

    context = {
        'form': my_form 
    }
    
    return render(request, 'products/product_create.html', context)
