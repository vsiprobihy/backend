from django.conf import settings
from django.db import models
from django.utils.timezone import now

from authentication.models import BaseProfile, CustomUser
from event.additional_items.models import AdditionalItemEvent
from event.distance_details.models import DistanceEvent
from event.models import Event
from event.promo_code.models import PromoCode
from user.managers import EventLikeManager


class AdditionalProfile(BaseProfile):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='additionalProfiles',
        on_delete=models.CASCADE,
    )
    email = models.EmailField()

    def __str__(self):
        return f'{self.firstName} {self.lastName} ({self.email})'


class UserDistanceRegistration(models.Model):
    registrationDate = models.DateTimeField(default=now)
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='distanceRegistrations'
    )
    distance = models.ForeignKey(
        DistanceEvent, on_delete=models.CASCADE, related_name='userRegistrations'
    )
    promoCode = models.ForeignKey(
        PromoCode, on_delete=models.SET_NULL, null=True, blank=True, related_name='registrations'
    )
    additionalItems = models.ManyToManyField(
        AdditionalItemEvent, blank=True, related_name='registrations'
    )
    # TODO: Add number
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    firstNameEng = models.CharField(max_length=50, null=True, blank=True)
    lastNameEng = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')], null=True)
    dateOfBirth = models.DateField(null=True)
    tShirtSize = models.CharField(
        max_length=5, choices=BaseProfile.T_SHIRT_SIZE_CHOICES, null=True
    )
    country = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=False)
    city = models.CharField(max_length=100, null=True)
    phoneNumber = models.CharField(max_length=20, null=True)
    sportsClub = models.CharField(max_length=100, null=True)
    emergencyContactName = models.CharField(max_length=100, null=True)
    emergencyContactPhone = models.CharField(max_length=20, null=True)

    class Meta:
        unique_together = ('user', 'distance')

    def __str__(self):
        return f'Registration of {self.firstName} for {self.distance.name}'


class EventLike(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='eventLikes')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='likes')
    liked_at = models.DateTimeField(auto_now_add=True)

    objects = EventLikeManager()

    class Meta:
        unique_together = ('user', 'event')

    def __str__(self):
        return f'{self.user.email} liked {self.event.name}'
