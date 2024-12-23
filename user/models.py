from django.db import models
from django.utils.timezone import now

from authentication.models import CustomUser
from event.distance_details.models import DistanceEvent
from event.models import Event
from user.managers import EventLikeManager


class UserDistanceRegistration(models.Model):
    registrationDate = models.DateTimeField(default=now)
    isConfirmed = models.BooleanField(default=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='distanceRegistrations')
    distance = models.ForeignKey(DistanceEvent, on_delete=models.CASCADE, related_name='userRegistrations')

    class Meta:
        unique_together = ('user', 'distance')

    def __str__(self):
        return f'Registration of {self.user.firstName} for {self.distance.name}'


class EventLike(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='eventLikes')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='likes')
    liked_at = models.DateTimeField(auto_now_add=True)

    objects = EventLikeManager()

    class Meta:
        unique_together = ('user', 'event')

    def __str__(self):
        return f'{self.user.email} liked {self.event.name}'
