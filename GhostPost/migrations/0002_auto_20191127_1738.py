# Generated by Django 2.2.6 on 2019-11-27 17:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('GhostPost', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='submit_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 27, 17, 38, 0, 850615, tzinfo=utc)),
        ),
    ]
