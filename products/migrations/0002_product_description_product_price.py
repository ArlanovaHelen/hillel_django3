# Generated by Django 4.2.7 on 2023-12-01 14:04

from django.db import migrations, models
import products.models.product


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(null=True, validators=[products.models.product.non_negative_validator]),
        ),
    ]
