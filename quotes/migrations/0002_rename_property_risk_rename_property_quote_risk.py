# Generated by Django 4.2.6 on 2023-10-22 12:45

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Property',
            new_name='Risk',
        ),
        migrations.RenameField(
            model_name='quote',
            old_name='property',
            new_name='risk',
        ),
    ]