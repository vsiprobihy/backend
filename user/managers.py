from django.db import models

from event.models import Event


class EventLikeManager(models.Manager):
    def like_event(self, user, event):
        from user.models import EventLike
        EventLike.objects.get_or_create(user=user, event=event)

    def unlike_event(self, user, event):
        from user.models import EventLike
        EventLike.objects.filter(user=user, event=event).delete()

    def get_liked_events(self, user):
        return Event.objects.filter(likes__user=user)
