
from rest_framework import serializers

from custom_admin.models import OrganizerRequest


class OrganizerRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizerRequest
        fields = ['id', 'user', 'isApproved', 'createdAt']
