# Generated by Django 2.2.3 on 2020-01-27 23:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estate_app', '0022_auto_20200127_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userphone', to='estate_app.Property'),
        ),
    ]
