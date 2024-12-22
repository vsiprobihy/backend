from rest_framework import serializers

from event.distance_details.serializers import DistanceEventSerializer
from user.models import UserDistanceRegistration


class UserDistanceRegistrationSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    distance = DistanceEventSerializer()

    class Meta:
        model = UserDistanceRegistration
        fields = ['id', 'user', 'distance', 'registrationDate', 'isConfirmed']
