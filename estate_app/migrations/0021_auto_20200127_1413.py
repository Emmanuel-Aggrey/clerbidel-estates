# Generated by Django 2.2.3 on 2020-01-27 14:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estate_app', '0020_auto_20200127_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
