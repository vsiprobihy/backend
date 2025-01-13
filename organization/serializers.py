from rest_framework import serializers

from authentication.models import CustomUser
from event.additional_items.serializers import AdditionalItemEventSerializer
from event.distance_details.serializers import PublicDistanceEventSerializer
from organization.models import Organization, Organizer
from user.models import UserDistanceRegistration
from utils.data_validatiors import validate_phone_number


class OrganizationSerializer(serializers.ModelSerializer):
    users = serializers.SerializerMethodField()
    phoneNumbers = serializers.ListField(child=serializers.CharField(max_length=20), allow_empty=True, required=False)

    class Meta:
        model = Organization
        fields = '__all__'

    def get_mainImage(self, obj):
        request = self.context.get('request')
        if obj.mainImage and request:
            return request.build_absolute_uri(obj.mainImage.url)
        return None

    def get_backgroundImage(self, obj):
        request = self.context.get('request')
        if obj.backgroundImage and request:
            return request.build_absolute_uri(obj.backgroundImage.url)
        return None

    def validate_phoneNumbers(self, value):
        for phone_number in value:
            validate_phone_number(phone_number)
        return value

    def get_users(self, obj):  # noqa
        access = Organizer.objects.filter(organization=obj)
        return [
            {
                'user': access_item.user.email,
                'role': access_item.user.role,
            }
            for access_item in access
        ]


class OrganizerSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='email', queryset=CustomUser.objects.all())
    organization = serializers.SlugRelatedField(slug_field='name', queryset=Organization.objects.all())

    class Meta:
        model = Organizer
        fields = ['id', 'user', 'organization']


class DistanceUserListSerializer(serializers.ModelSerializer):
    distance = PublicDistanceEventSerializer()
    additionalItems = AdditionalItemEventSerializer(many=True)

    class Meta:
        model = UserDistanceRegistration
        fields = ['id', 'firstName', 'startingNumber', 'city', 'gender',
                  'dateOfBirth', 'sportsClub', 'distance', 'additionalItems'
                  ]


class DistanceUserDetailSerializer(serializers.ModelSerializer):
    distance = PublicDistanceEventSerializer(read_only=True)
    additionalItems = AdditionalItemEventSerializer(many=True, read_only=True)

    class Meta:
        model = UserDistanceRegistration
        fields = [
            'id', 'registrationDate', 'email', 'firstName', 'lastName', 'firstNameEng', 'lastNameEng',
            'gender', 'dateOfBirth', 'tShirtSize', 'country', 'city', 'phoneNumber', 'sportsClub',
            'emergencyContactName', 'emergencyContactPhone', 'distance', 'additionalItems'
        ]
        extra_kwargs = {
            'user': {'read_only': True},
            'promoCode': {'read_only': True},
        }
