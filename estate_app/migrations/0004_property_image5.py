# Generated by Django 2.2.3 on 2019-12-31 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate_app', '0003_auto_20191231_0107'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='image5',
            field=models.FileField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/'),
        ),
    ]
