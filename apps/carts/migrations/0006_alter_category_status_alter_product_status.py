# Generated by Django 5.1.5 on 2025-01-19 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0005_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], default='True', max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], default='True', max_length=10),
        ),
    ]
