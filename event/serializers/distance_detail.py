from rest_framework import serializers

from event.models import AdditionalItemEvent, DistanceEvent, Event
from event.serializers.additional_items import AdditionalItemEventSerializer


class DistanceEventSerializer(serializers.ModelSerializer):
    event = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all(), required=False)
    additional_options = AdditionalItemEventSerializer(many=True, required=False)

    class Meta:
        model = DistanceEvent
        fields = [
            'id', 'name', 'competition_type', 'category', 'allow_registration',
            'length', 'start_number_from', 'start_number_to', 'age_from', 'age_to',
            'cost', 'is_free', 'promo_only_registration',
            'show_name_on_number', 'show_start_number', 'event', 'additional_options'
        ]
        extra_kwargs = {'event': {'read_only': True}}

    def create(self, validated_data):
        additional_options_data = validated_data.pop('additional_options', [])
        distance = DistanceEvent.objects.create(**validated_data)

        for option_data in additional_options_data:
            option_data['event'] = distance.event
            option_data['distance'] = distance
            AdditionalItemEvent.objects.create(**option_data)

        return distance

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.competition_type = validated_data.get('competition_type', instance.competition_type)
        instance.category = validated_data.get('category', instance.category)
        instance.length = validated_data.get('length', instance.length)
        instance.start_number_from = validated_data.get('start_number_from', instance.start_number_from)
        instance.start_number_to = validated_data.get('start_number_to', instance.start_number_to)
        instance.age_from = validated_data.get('age_from', instance.age_from)
        instance.age_to = validated_data.get('age_to', instance.age_to)
        instance.cost = validated_data.get('cost', instance.cost)
        instance.is_free = validated_data.get('is_free', instance.is_free)
        instance.promo_only_registration = validated_data.get('promo_only_registration', instance.promo_only_registration)  # noqa: E501
        instance.show_name_on_number = validated_data.get('show_name_on_number', instance.show_name_on_number)
        instance.show_start_number = validated_data.get('show_start_number', instance.show_start_number)

        instance.save()

        additional_options_data = validated_data.get('additional_options', [])
        for option_data in additional_options_data:
            option_id = option_data.get('id')
            if option_id:
                option = AdditionalItemEvent.objects.get(id=option_id)
                option_serializer = AdditionalItemEventSerializer(option, data=option_data, partial=True)
                if option_serializer.is_valid():
                    option_serializer.save()
            else:
                option_data['event'] = instance.event
                option_data['distance'] = instance
                AdditionalItemEvent.objects.create(**option_data)

        return instance
