# Generated by Django 4.2.16 on 2024-11-04 07:44

import authentication.models
from django.db import migrations, models
import utils.data_validatiors


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0011_alter_customuser_emergency_contact_phone"),
    ]

    operations = [
        migrations.AddField(
            model_name="additionalprofile",
            name="avatar",
            field=models.ImageField(
                blank=True,
                max_length=255,
                null=True,
                upload_to=authentication.models.customer_image_file_path,
            ),
        ),
        migrations.AddField(
            model_name="additionalprofile",
            name="city",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="additionalprofile",
            name="country",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="additionalprofile",
            name="date_of_birth",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="additionalprofile",
            name="emergency_contact_name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="additionalprofile",
            name="emergency_contact_phone",
            field=models.CharField(
                blank=True,
                max_length=20,
                null=True,
                unique=True,
                validators=[utils.data_validatiors.validate_phone_number],
                verbose_name="phone number",
            ),
        ),
        migrations.AddField(
            model_name="additionalprofile",
            name="first_name_eng",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="additionalprofile",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[("M", "Male"), ("F", "Female")],
                max_length=10,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="additionalprofile",
            name="last_name_eng",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="additionalprofile",
            name="phone_number",
            field=models.CharField(
                blank=True,
                max_length=20,
                null=True,
                unique=True,
                validators=[utils.data_validatiors.validate_phone_number],
                verbose_name="phone number",
            ),
        ),
        migrations.AddField(
            model_name="additionalprofile",
            name="sports_club",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="additionalprofile",
            name="t_shirt_size",
            field=models.CharField(
                blank=True,
                choices=[
                    ("XXS", "Very Extra Small"),
                    ("XS", "Extra Small"),
                    ("S", "Small"),
                    ("M", "Medium"),
                    ("L", "Large"),
                    ("XL", "Extra Large"),
                    ("XXL", "Extra Extra Large"),
                    ("XXXL", "Very Extra Extra Large"),
                ],
                max_length=5,
                null=True,
            ),
        ),
    ]
