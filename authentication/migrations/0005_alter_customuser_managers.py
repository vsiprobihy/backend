# Generated by Django 4.2.16 on 2024-10-26 09:10

import authentication.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0004_customuser_role"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="customuser",
            managers=[
                ("objects", authentication.managers.CustomUserManager()),
            ],
        ),
    ]
