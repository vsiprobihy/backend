from rest_framework import serializers

from event.promo_code.models import PromoCode


class PromoCodeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = PromoCode
        fields = ['id', 'name', 'promoType', 'discountValue', 'isActive', 'isSingleUse', 'distance']
        extra_kwargs = {
            'distance': {'read_only': True}
        }
