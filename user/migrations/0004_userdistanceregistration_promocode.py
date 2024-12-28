# Generated by Django 4.2.16 on 2024-12-28 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('promo_code', '0001_initial'),
        ('user', '0003_remove_userdistanceregistration_isconfirmed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdistanceregistration',
            name='promoCode',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='registrations', to='promo_code.promocode'),
        ),
    ]