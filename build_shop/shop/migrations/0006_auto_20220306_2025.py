# Generated by Django 3.2 on 2022-03-06 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='products/%Y/%m/%d/<django.db.models.fields.CharField>'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='', max_length=200, unique=True),
        ),
    ]
