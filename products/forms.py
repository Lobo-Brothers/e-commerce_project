from django import forms
from .models import Product, Category
from mptt.forms import TreeNodeChoiceField
from django.forms.fields import ImageField

class ProductForm(forms.Form):
    title       = forms.CharField(
            label='', 
            widget=forms.TextInput(
            attrs={
                'placeholder': 'Your title'
            }
        )
    )
    image       = forms.ImageField()
    description = forms.CharField(
            required=False,
            widget=forms.Textarea(
                attrs={
                    #'class': aca va una clase en el caso que la quieras usar
                    #'id': y aca la id
                    'rows': 5,
                    'cols': 10,
                    'placeholder': 'Describe your product :)'

            }
        )
    )
    category    = TreeNodeChoiceField(queryset=Category.objects.all())
    price       = forms.DecimalField(initial=69.99)