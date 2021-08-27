# Generated by Django 3.2.6 on 2021-08-27 02:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='offer_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True, validators=[django.core.validators.MinValueValidator(0.01)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='preview',
            field=models.CharField(choices=[('slider', 'Slider'), ('pre-order', 'Pre-order'), ('new', 'New'), ('offer', 'Offer'), ('hidden', 'Hidden')], default='hidden', max_length=10),
        ),
    ]