# Generated by Django 4.0.1 on 2022-02-24 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0002_entry_hours_entry_minutes_entry_seconds'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='solve_time',
        ),
    ]
