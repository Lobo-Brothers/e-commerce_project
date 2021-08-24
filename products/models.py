from products.choices import CATEGORY_CHOICES, PREVIEW_CHOICES
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from random import randint


# Create your models here.
class CustomQuerySet(models.QuerySet):
    def on_slider(self):
        return self.filter(preview='slider')

    def on_preorder(self):
        return self.filter(preview='preorder')

    def get_accesories(self):
        return self.filter(category='accesory')

    def get_hoodies(self):
        return self.filter(category='hoodie')

    def get_bottoms(self):
        return self.filter(category='bottom')

    def get_sneakers(self):
        return self.filter(category='sneaker')

    def get_outerwears(self):
        return self.filter(category='outerwear')

    def get_tshirts(self):
        return self.filter(category='t-shirt')

    def random(self):
        random = self
        if len(random) > 0:
            return random[randint(0, len(random) - 1)]

        #Hacer esto me tomo una noche entera y una lata de speed


class Product(models.Model):
    title           = models.CharField(max_length=128)
    image           = models.ImageField(upload_to='images')
    description     = models.TextField(blank=True, null=True)
    category        = models.CharField(max_length=16, choices=CATEGORY_CHOICES)
    price           = models.DecimalField(decimal_places=2, max_digits=9)
    featured        = models.BooleanField(default=False)
    preview         = models.CharField(default='hidden', max_length=10, choices=PREVIEW_CHOICES)
    custom_category = TreeForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)

    objects     = CustomQuerySet.as_manager()
    
    def __str__(self):
        return f'{self.category}, {self.title}'

class Category(MPTTModel):
    name    = models.CharField(max_length=50, unique=True)
    parent  = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='child')
    slug    = models.SlugField()

    class MPTTMeta:
        order_insertion_by= ['name']

    class Meta:
        verbose_name_plural= 'Categories'
        unique_together = (('parent', 'slug',))

    def __str__(self):
        return self.name
