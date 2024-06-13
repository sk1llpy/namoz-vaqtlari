# Generated by Django 4.0 on 2024-06-01 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_users_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='region',
            field=models.CharField(blank=True, default='Toshkent', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='tasbih_counter',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
