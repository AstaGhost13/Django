# Generated by Django 5.1.6 on 2025-03-09 00:02

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hierarchy', '0001_initial'),
        ('inventory', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AsignacionProduct',
            new_name='ProductAssignment',
        ),
    ]
