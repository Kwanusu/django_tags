# Generated by Django 5.2.3 on 2025-06-23 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_tags', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='is_active',
        ),
    ]
