# Generated by Django 5.1.5 on 2025-01-19 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0006_alter_category_status_alter_product_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
