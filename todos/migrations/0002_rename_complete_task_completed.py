# Generated by Django 4.2.2 on 2023-06-24 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='complete',
            new_name='completed',
        ),
    ]
