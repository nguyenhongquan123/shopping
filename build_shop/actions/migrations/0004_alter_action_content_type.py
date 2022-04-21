# Generated by Django 3.2 on 2022-04-08 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('actions', '0003_alter_comment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='action', to='contenttypes.contenttype'),
        ),
    ]