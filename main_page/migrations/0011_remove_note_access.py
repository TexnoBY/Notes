# Generated by Django 3.1.2 on 2020-11-06 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0010_auto_20201103_2134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='access',
        ),
    ]
