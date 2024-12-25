# Generated by Django 5.1 on 2024-12-17 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accou', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSignup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('area', models.CharField(max_length=100)),
                ('timing', models.TimeField()),
            ],
        ),
    ]