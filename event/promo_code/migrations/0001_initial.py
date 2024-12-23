# Generated by Django 4.2.16 on 2024-12-21 17:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('distance_details', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PromoCode',
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
                ('name', models.CharField(max_length=255)),
                (
                    'promoType',
                    models.CharField(
                        choices=[
                            ('flat', 'Flat Discount'),
                            ('percentage', 'Percentage Discount'),
                            ('sum_registration', 'Sum Registration Discount'),
                            ('free', 'Free Discount'),
                        ],
                        max_length=20,
                    ),
                ),
                ('discountValue', models.DecimalField(decimal_places=2, max_digits=10)),
                ('isActive', models.BooleanField(default=False)),
                ('isSingleUse', models.BooleanField(default=False)),
                (
                    'distance',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='promoCodes',
                        to='distance_details.distanceevent',
                    ),
                ),
            ],
        ),
    ]
