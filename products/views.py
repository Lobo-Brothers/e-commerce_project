from django.shortcuts import render

from .forms import ProductForm 

# Create your views here.

def product_create_view(request):
    my_form = ProductForm(request.POST, request.FILES)
    if request.method == "POST":
        if my_form.is_valid():
            Product.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)

    context = {
        'form': my_form 
    }
    
    return render(request, 'products/product_create.html', context)
