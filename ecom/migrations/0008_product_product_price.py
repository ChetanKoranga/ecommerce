# Generated by Django 3.0.5 on 2020-05-13 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0007_auto_20200512_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_price',
            field=models.IntegerField(default=True),
        ),
    ]