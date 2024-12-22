from django.urls import path

from .views import (
    AdditionalProfileDetailView,
    AdditionalProfileListView,
    LikedEventsView,
    LikeEventView,
    RequestOrganizerView,
    UserDistanceRegistrationView,
    UserProfileView,
)


urlpatterns = [
    path('request-organizer/', RequestOrganizerView.as_view(), name='request-organizer'),
    path('distance/<int:distance_id>/register/', UserDistanceRegistrationView.as_view(), name='register-distance'),
    path(
        'profile/additional-profiles/',
        AdditionalProfileListView.as_view(),
        name='additional_profiles_list',
    ),
    path(
        'profile/additional-profiles/<int:id>/',
        AdditionalProfileDetailView.as_view(),
        name='additional_profile_detail',
    ),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('events/<int:event_id>/like/', LikeEventView.as_view(), name='like-event'),
    path('events/liked/', LikedEventsView.as_view(), name='liked-events'),
]
