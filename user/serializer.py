from rest_framework import serializers

from user.models import UserDistanceRegistration


class UserDistanceRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDistanceRegistration
        fields = [
            'id', 'registrationDate','email',
            'firstName', 'lastName', 'firstNameEng', 'lastNameEng', 'gender',
            'dateOfBirth', 'tShirtSize', 'country', 'city', 'phoneNumber',
            'sportsClub', 'emergencyContactName', 'emergencyContactPhone'
        ]
        read_only_fields = ['user', 'distance']
