from rest_framework import serializers

from event.additional_items.models import AdditionalItemEvent
from event.promo_code.models import PromoCode
from user.models import AdditionalProfile, UserDistanceRegistration


class UserDistanceRegistrationSerializer(serializers.ModelSerializer):
    promoCode = serializers.PrimaryKeyRelatedField(
        queryset=PromoCode.objects.filter(isActive=True), required=False
    )
    additionalItems = serializers.PrimaryKeyRelatedField(
        many=True, queryset=AdditionalItemEvent.objects.all(), required=False
    )

    # TODO: Add startingNumber
    # startingNumber
    class Meta:
        model = UserDistanceRegistration
        fields = [
            'id', 'registrationDate', 'email', 'firstName', 'lastName', 'firstNameEng', 'lastNameEng',
            'gender', 'dateOfBirth', 'tShirtSize', 'country', 'city', 'phoneNumber', 'sportsClub',
            'emergencyContactName', 'emergencyContactPhone', 'promoCode', 'additionalItems'
        ]
        read_only_fields = ['user', 'distance']


class AdditionalProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalProfile
        fields = [
            'id', 'firstName', 'lastName', 'firstNameEng', 'lastNameEng',
            'gender', 'dateOfBirth', 'tShirtSize', 'country', 'city',
            'phoneNumber', 'sportsClub', 'emergencyContactName',
            'emergencyContactPhone', 'email'
        ]

    def validate(self, attrs):
        user = self.context['request'].user
        if user.additionalProfiles.count() >= 5:
            raise serializers.ValidationError('User cannot have more than 5 additional profiles.')
        return attrs

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
