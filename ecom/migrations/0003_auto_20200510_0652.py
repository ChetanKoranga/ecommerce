# Generated by Django 3.0.5 on 2020-05-10 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0002_auto_20200510_0647'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='SubCategory_name',
            new_name='Subcategory_name',
        ),
    ]
