# Generated by Django 3.1.2 on 2020-11-02 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0004_auto_20201102_1603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='photo',
        ),
    ]
