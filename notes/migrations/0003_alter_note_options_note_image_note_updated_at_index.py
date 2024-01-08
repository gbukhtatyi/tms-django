# Generated by Django 5.0 on 2024-01-08 05:12

import notes.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_note_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['-updated_at']},
        ),
        migrations.AddField(
            model_name='note',
            name='image',
            field=models.ImageField(null=True, upload_to=notes.models.upload_to),
        ),
        migrations.AddIndex(
            model_name='note',
            index=models.Index(fields=['updated_at'], name='updated_at_index'),
        ),
    ]