# Generated by Django 3.2 on 2022-04-08 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0002_auto_20220408_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
