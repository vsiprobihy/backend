# Generated by Django 4.2.16 on 2024-12-31 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_remove_additionalprofile_avatar'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AdditionalProfile',
        ),
    ]