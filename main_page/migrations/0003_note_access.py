# Generated by Django 3.1.2 on 2020-10-29 12:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_page', '0002_auto_20201024_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='access',
            field=models.ManyToManyField(related_name='access', to=settings.AUTH_USER_MODEL),
        ),
    ]
