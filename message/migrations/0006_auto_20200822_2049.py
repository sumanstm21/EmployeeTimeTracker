# Generated by Django 3.0.8 on 2020-08-22 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0005_auto_20200822_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date Created'),
        ),
    ]