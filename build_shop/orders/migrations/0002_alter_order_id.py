# Generated by Django 3.2 on 2022-03-16 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.CharField(max_length=12, primary_key=True, serialize=False),
        ),
    ]