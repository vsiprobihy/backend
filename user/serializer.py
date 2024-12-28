from rest_framework import serializers

from event.additional_items.models import AdditionalItemEvent
from event.promo_code.models import PromoCode
from user.models import UserDistanceRegistration


class UserDistanceRegistrationSerializer(serializers.ModelSerializer):
    promoCode = serializers.PrimaryKeyRelatedField(
        queryset=PromoCode.objects.filter(isActive=True), required=False
    )
    additionalItems = serializers.PrimaryKeyRelatedField(
        many=True, queryset=AdditionalItemEvent.objects.all(), required=False
    )

    class Meta:
        model = UserDistanceRegistration
        fields = [
            'id', 'registrationDate', 'email', 'firstName', 'lastName', 'firstNameEng', 'lastNameEng',
            'gender', 'dateOfBirth', 'tShirtSize', 'country', 'city', 'phoneNumber', 'sportsClub',
            'emergencyContactName', 'emergencyContactPhone', 'promoCode', 'additionalItems'
        ]
        read_only_fields = ['user', 'distance']
