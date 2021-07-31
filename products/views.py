from django.shortcuts import render

# Create your views here.

def product_create_view(request):
    return render(request, 'products/product_create.html')