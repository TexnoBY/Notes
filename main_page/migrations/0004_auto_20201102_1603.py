# Generated by Django 3.1.2 on 2020-11-02 13:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_page', '0003_note_access'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='access',
            field=models.ManyToManyField(default=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_note', to=settings.AUTH_USER_MODEL), related_name='access', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth', models.DateTimeField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, upload_to='user/%Y/%m/%d/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
