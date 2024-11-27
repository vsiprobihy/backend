# Generated by Django 4.2.16 on 2024-11-27 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_alter_event_competition_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending approval'), ('unpublished', 'Unpublished'), ('published', 'Published')], db_index=True, default='pending', max_length=12),
        ),
    ]
