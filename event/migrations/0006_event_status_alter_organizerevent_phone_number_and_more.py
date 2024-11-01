# Generated by Django 4.2.16 on 2024-10-15 19:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0005_remove_eventregistration_distance_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('pending', 'Очікує затвердження'), ('unpublished', 'Не опублікована'), ('published', 'Опублікована')], default='pending', max_length=12),
        ),
        migrations.AlterField(
            model_name='organizerevent',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='OrganizationAccess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('owner', 'Owner'), ('organizer', 'Organizer')], max_length=10)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_access', to='event.organizerevent')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization_access', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'organization')},
            },
        ),
    ]
