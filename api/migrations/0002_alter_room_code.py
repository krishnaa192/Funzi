# Generated by Django 3.2.15 on 2023-04-11 19:20

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='code',
            field=models.CharField(default=api.models.genrate_random_code, max_length=8, unique=True),
        ),
    ]
