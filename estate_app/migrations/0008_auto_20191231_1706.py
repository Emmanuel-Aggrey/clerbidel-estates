# Generated by Django 2.2.3 on 2019-12-31 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate_app', '0007_auto_20191231_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='position',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
