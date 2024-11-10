# Generated by Django 4.2.16 on 2024-10-29 18:53

from django.db import migrations, models
import utils.data_validatiors


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0006_customuser_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="phone_number",
            field=models.CharField(
                max_length=20,
                null=True,
                unique=True,
                validators=[utils.data_validatiors.validate_phone_number],
                verbose_name="phone number",
            ),
        ),
    ]
