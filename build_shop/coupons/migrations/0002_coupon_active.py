# Generated by Django 3.2 on 2022-03-27 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='active',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
