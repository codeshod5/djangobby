# Generated by Django 5.1 on 2024-12-17 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accou', '0003_remove_usersignup_area_remove_usersignup_timing'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersignup',
            name='area',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usersignup',
            name='timing',
            field=models.TimeField(default=None),
            preserve_default=False,
        ),
    ]
