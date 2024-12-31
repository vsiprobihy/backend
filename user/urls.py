from django.urls import path

from user.views import (
    AdditionalProfileDetailView,
    AdditionalProfileListView,
    LikedEventsView,
    LikeEventView,
    RequestOrganizerView,
    UserDistanceRegistrationsView,
    UserDistanceRegistrationView,
    UserProfileView,
)


urlpatterns = [
    path('request-organizer/', RequestOrganizerView.as_view(), name='request-organizer'),
    path('distance/<int:distance_id>/register/', UserDistanceRegistrationView.as_view(), name='register-distance'),
    path('distance/register/', UserDistanceRegistrationsView.as_view(), name='user-registrations'),
    path(
        'profile/additional-profile/',
        AdditionalProfileListView.as_view(),
        name='additional_profiles_list',
    ),
    path(
        'profile/additional-profile/<int:profile_id>/',
        AdditionalProfileDetailView.as_view(),
        name='additional_profile_detail',
    ),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('event/<int:event_id>/like/', LikeEventView.as_view(), name='like-event'),
    path('event/like/', LikedEventsView.as_view(), name='liked-event'),
]
