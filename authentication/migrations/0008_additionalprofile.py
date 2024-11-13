# Generated by Django 4.2.16 on 2024-10-29 20:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_alter_customuser_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalProfile',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                (
                    'user',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='additional_profiles',
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
