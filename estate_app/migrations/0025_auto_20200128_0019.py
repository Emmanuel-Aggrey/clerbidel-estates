# Generated by Django 2.2.3 on 2020-01-28 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate_app', '0024_auto_20200127_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='created_by',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
