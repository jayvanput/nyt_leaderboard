# Generated by Django 4.0.1 on 2022-04-21 03:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0014_alter_entry_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='created',
            field=models.DateField(default=datetime.date(2022, 4, 20)),
        ),
    ]
