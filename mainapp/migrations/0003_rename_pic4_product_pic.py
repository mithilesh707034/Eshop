# Generated by Django 4.1.1 on 2022-11-04 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_alter_buyer_pic_alter_product_pic1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='pic4',
            new_name='pic',
        ),
    ]
