# Generated by Django 3.0.6 on 2020-06-12 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0011_auto_20200612_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cate_blog', to='blogs.Category'),
        ),
    ]