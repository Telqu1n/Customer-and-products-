# Generated by Django 5.1.2 on 2024-12-12 10:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Products'},
        ),
        migrations.AddField(
            model_name='customer',
            name='Product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customers', to='customer_app.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(max_length=10),
        ),
    ]