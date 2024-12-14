# Generated by Django 4.2.16 on 2024-11-27 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('distance_details', '0002_costchangerule'),
    ]

    operations = [
        migrations.CreateModel(
            name='PromoCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('promo_type', models.CharField(choices=[('flat', 'Flat Discount'), ('percentage', 'Percentage Discount'), ('sum_registration', 'Sum Registration Discount'), ('free', 'Free Discount')], max_length=20)),
                ('discount_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_active', models.BooleanField(default=False)),
                ('is_single_use', models.BooleanField(default=False)),
                ('distance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='promo_codes', to='distance_details.distanceevent')),
            ],
        ),
    ]