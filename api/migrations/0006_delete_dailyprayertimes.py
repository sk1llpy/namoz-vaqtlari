# Generated by Django 4.0 on 2024-06-11 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_users_tasbih_mode'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DailyPrayerTimes',
        ),
    ]
