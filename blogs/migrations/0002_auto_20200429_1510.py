# Generated by Django 3.0.5 on 2020-04-29 08:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
