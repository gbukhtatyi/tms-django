# Generated by Django 5.0.2 on 2024-02-19 06:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_alter_event_meeting_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='meeting_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
