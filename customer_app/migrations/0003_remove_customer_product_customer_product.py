# Generated by Django 5.1.2 on 2024-12-12 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_app', '0002_alter_product_options_customer_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='Product',
        ),
        migrations.AddField(
            model_name='customer',
            name='Product',
            field=models.ManyToManyField(to='customer_app.product'),
        ),
    ]