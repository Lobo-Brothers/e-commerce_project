# Generated by Django 3.2.5 on 2021-08-24 05:10

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField()),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child', to='products.category')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'unique_together': {('parent', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('image', models.ImageField(upload_to='images')),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.CharField(choices=[('accesory', 'Accesory'), ('bottom', 'Bottoms'), ('hoodie', 'Hoodies'), ('outerwear', 'Outerwears'), ('sneaker', 'Sneakers'), ('t-shirt', 'T-Shirts')], max_length=16)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('featured', models.BooleanField(default=False)),
                ('preview', models.CharField(choices=[('slider', 'Slider'), ('pre-order', 'Pre-order'), ('hidden', 'Hidden')], default='hidden', max_length=10)),
                ('custom_category', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
        ),
    ]
