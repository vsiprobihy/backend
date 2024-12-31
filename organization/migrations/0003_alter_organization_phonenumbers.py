import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_alter_organization_phonenumbers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='phoneNumbers',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), blank=True, default=list, size=None),
        ),
    ]
