# Generated by Django 2.2.3 on 2020-01-17 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate_app', '0015_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('image', models.FileField(upload_to='gallary/%Y/%m/%d/')),
            ],
        ),
    ]
