# Generated by Django 2.2.3 on 2019-08-01 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chinook', '0005_auto_20190801_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='media_type',
            field=models.ManyToManyField(through='chinook.Track', to='chinook.MediaType'),
        ),
    ]
