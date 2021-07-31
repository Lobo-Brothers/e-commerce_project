from django.db import models

# Create your models here.

class Product(models.Model):
    title       = models.CharField(max_length=128)
    image       = models.ImageField(upload_to='images')
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=9)
    featured    = models.BooleanField()
    
    def __str__(self):
        return self.title