# Generated by Django 5.1 on 2024-12-14 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buses', '0003_addroutes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userlocred',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userarea', models.TextField()),
                ('usertiming', models.TimeField()),
            ],
        ),
    ]