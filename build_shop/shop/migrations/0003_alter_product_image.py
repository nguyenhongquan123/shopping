# Generated by Django 3.2 on 2022-03-06 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20220306_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='products/%Y%m%d/<django.db.models.fields.SlugField>'),
        ),
    ]