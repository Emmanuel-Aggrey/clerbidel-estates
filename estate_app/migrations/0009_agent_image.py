# Generated by Django 2.2.3 on 2019-12-31 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate_app', '0008_auto_20191231_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='profiles/%Y/%m/%d/'),
        ),
    ]
