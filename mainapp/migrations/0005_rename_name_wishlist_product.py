# Generated by Django 4.1.1 on 2022-11-19 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_wishlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishlist',
            old_name='name',
            new_name='product',
        ),
    ]