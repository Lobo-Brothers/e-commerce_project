from django.shortcuts import render

from .forms import ProductForm 
from .models import Product
from django.shortcuts import redirect

# Create your views here.

def product_create_view(request):

    if request.user.is_superuser:
        my_form = ProductForm(request.POST, request.FILES)
        if request.method == "POST":
            if my_form.is_valid():
                Product.objects.create(**my_form.cleaned_data)

        context = {
            'form': my_form 
        }

        return render(request, 'products/product_create.html', context)
    else:
        return redirect('/')
