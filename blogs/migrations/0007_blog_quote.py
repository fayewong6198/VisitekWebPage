# Generated by Django 3.0.6 on 2020-06-04 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_auto_20200603_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='quote',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
