from django.urls import path

from custom_admin.views import (
    ApproveOrganizerView,
    CompetitionsTypeDetailView,
    CompetitionsTypeListCreateView,
    OrganizerRequestsListView,
    PendingEventsView,
    UpdateEventStatusView,
)


urlpatterns = [
    path('competition-type/', CompetitionsTypeListCreateView.as_view(), name='competitions-type-list'),
    path('competition-type/<int:competition_type_id>/', CompetitionsTypeDetailView.as_view(),
         name='competition-type-detail'),
    path('user/<int:user_id>/approve-organizer/', ApproveOrganizerView.as_view(), name='approve-organizer'),
    path('event/<int:event_id>/update-status/', UpdateEventStatusView.as_view(), name='update-event-status'),
    path('event/update-status-request/', PendingEventsView.as_view(), name='pending-events'),
    path('organizer-request/', OrganizerRequestsListView.as_view(), name='organizer-request-list'),
]
