# Generated by Django 2.2.7 on 2019-11-30 03:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('GhostPost', '0002_auto_20191127_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='submit_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
