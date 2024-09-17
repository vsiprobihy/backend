# Generated by Django 4.2.16 on 2024-09-16 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_remove_organizerevent_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventregistration',
            name='additional_items',
            field=models.ManyToManyField(blank=True, related_name='registrations', to='event.additionalitemevent'),
        ),
        migrations.AddField(
            model_name='eventregistration',
            name='distance',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='registrations', to='event.distanceevent'),
        ),
    ]