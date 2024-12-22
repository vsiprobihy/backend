
from rest_framework import serializers

from custom_admin.models import OrganizerRequest
from event.models import Event


class OrganizerRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizerRequest
        fields = ['id', 'user', 'isApproved', 'createdAt']


class RequestStatusEventSerializer(serializers.ModelSerializer):
    organizer = serializers.CharField(source='organization.name')  # Якщо потрібно вивести ім'я організації

    class Meta:
        model = Event
        fields = ['id', 'name', 'organizer', 'competitionType', 'dateFrom', 'dateTo', 'status']
