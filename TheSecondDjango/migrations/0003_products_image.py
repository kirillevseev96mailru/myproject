# Generated by Django 4.2.3 on 2023-09-12 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TheSecondDjango', '0002_remove_orders_name_product_orders_name_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
