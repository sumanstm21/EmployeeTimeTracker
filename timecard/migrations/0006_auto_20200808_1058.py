# Generated by Django 3.0.8 on 2020-08-08 08:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timecard', '0005_auto_20200808_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailylog',
            name='checkin_time',
            field=models.DateTimeField(default=datetime.datetime.now, max_length=100),
        ),
        migrations.AlterField(
            model_name='dailylog',
            name='checkout_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]
