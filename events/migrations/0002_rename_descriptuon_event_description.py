# Generated by Django 5.0.2 on 2024-02-18 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='descriptuon',
            new_name='description',
        ),
    ]
