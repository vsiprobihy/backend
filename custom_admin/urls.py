from django.urls import include, path
from rest_framework.routers import DefaultRouter

from custom_admin.views import (
    ApproveOrganizerView,
    CompetitionsTypeViewSet,
    OrganizerRequestsListView,
    PendingEventsView,
    UpdateEventStatusView,
)


router = DefaultRouter()
router.register(r'competitions-type', CompetitionsTypeViewSet, basename='competitions_type')

urlpatterns = [
    path('', include(router.urls)),
    path('user/<int:user_id>/approve-organizer/', ApproveOrganizerView.as_view(), name='approve-organizer'),
    path('event/<int:event_id>/update-status/', UpdateEventStatusView.as_view(), name='update-event-status'),
    path('events/update-status-requests/', PendingEventsView.as_view(), name='pending-events'),
    path('organizer-requests/', OrganizerRequestsListView.as_view(), name='organizer-requests-list'),
]
