# Generated by Django 4.2.16 on 2024-11-16 21:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompetitionType',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=255)),
                ('date_from', models.DateField()),
                ('date_to', models.DateField()),
                (
                    'place_region',
                    models.CharField(
                        choices=[
                            ('vinnytsia_region', 'Vinnytsia oblast'),
                            ('volyn_region', 'Volyn oblast'),
                            ('dnipropetrovsk_region', 'Dnipropetrovsk oblast'),
                            ('donetsk_region', 'Donetsk oblast'),
                            ('zhytomyr_region', 'Zhytomyr oblast'),
                            ('zakarpattia_region', 'Zakarpattia oblast'),
                            ('zaporizhzhia_region', 'Zaporizhzhia oblast'),
                            ('ivano-frankivsk_region', 'Ivano-Frankivsk oblast'),
                            ('kyiv_region', 'Kyiv oblast'),
                            ('kirovohrad_region', 'Kirovohrad oblast'),
                            ('luhansk_region', 'Luhansk oblast'),
                            ('lviv_region', 'Lviv oblast'),
                            ('mykolaiv_region', 'Mykolaiv oblast'),
                            ('odesa_region', 'Odesa oblast'),
                            ('poltava_region', 'Poltava oblast'),
                            ('rivne_region', 'Rivne oblast'),
                            ('sumy_region', 'Sumy oblast'),
                            ('ternopil_region', 'Ternopil oblast'),
                            ('kharkiv_region', 'Kharkiv oblast'),
                            ('kherson_region', 'Kherson oblast'),
                            ('khmelnytskyi_region', 'Khmelnytskyi oblast'),
                            ('cherkasy_region', 'Cherkasy oblast'),
                            ('chernihiv_region', 'Chernihiv oblast'),
                            ('chernivtsi_region', 'Chernivtsi oblast'),
                        ],
                        max_length=255,
                        null=True,
                    ),
                ),
                ('place', models.CharField(max_length=255)),
                (
                    'photos',
                    models.ImageField(blank=True, null=True, upload_to='event_photos/'),
                ),
                ('description', models.TextField()),
                ('registration_link', models.URLField(blank=True, null=True)),
                ('hide_participants', models.BooleanField(default=False)),
                ('extended_description', models.TextField(blank=True, null=True)),
                (
                    'schedule_pdf',
                    models.FileField(
                        blank=True, null=True, upload_to='event_schedule/'
                    ),
                ),
                (
                    'status',
                    models.CharField(
                        choices=[
                            ('pending', 'Pending approval'),
                            ('unpublished', 'Unpublished'),
                            ('published', 'Published'),
                        ],
                        default='pending',
                        max_length=12,
                    ),
                ),
                (
                    'competition_type',
                    models.ManyToManyField(
                        related_name='events', to='organizer_event.competitiontype'
                    ),
                ),
                (
                    'organizer',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='events',
                        to='organization.organizerevent',
                    ),
                ),
            ],
        ),
    ]