# Generated by Django 4.2.16 on 2024-12-31 11:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utils.data_validatiors


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0005_userdistanceregistration_additionalitems'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('firstNameEng', models.CharField(max_length=50)),
                ('lastNameEng', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10)),
                ('dateOfBirth', models.DateField()),
                ('tShirtSize', models.CharField(choices=[('XXS', 'Very Extra Small'), ('XS', 'Extra Small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large'), ('XXL', 'Extra Extra Large'), ('XXXL', 'Very Extra Extra Large')], max_length=5, null=True)),
                ('country', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('phoneNumber', models.CharField(max_length=20, validators=[utils.data_validatiors.validate_phone_number], verbose_name='phone number')),
                ('sportsClub', models.CharField(max_length=100)),
                ('emergencyContactName', models.CharField(max_length=100)),
                ('emergencyContactPhone', models.CharField(max_length=20, validators=[utils.data_validatiors.validate_phone_number], verbose_name='phone number')),
                ('email', models.EmailField(max_length=254)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='additionalProfiles', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
