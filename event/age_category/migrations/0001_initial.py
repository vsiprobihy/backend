# Generated by Django 4.2.16 on 2024-11-27 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('distance_details', '0002_costchangerule'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10)),
                ('age_from', models.PositiveIntegerField()),
                ('age_to', models.PositiveIntegerField()),
                ('distance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='age_categories', to='distance_details.distanceevent')),
            ],
        ),
    ]