# Generated by Django 3.0.8 on 2020-08-27 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginmanager', '0007_auto_20200827_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='monthly_salary',
            field=models.FloatField(blank=True, help_text='Monthly Salary', null=True),
        ),
    ]