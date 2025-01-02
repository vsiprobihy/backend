from django.urls import path

from organization.views import (
    DistanceUserDetailView,
    DistanceUserListView,
    InviteOrganizerView,
    OrganizationDetailView,
    OrganizationListCreateView,
)


urlpatterns = [
    path('', OrganizationListCreateView.as_view(), name='organization-list-create'),
    path('<int:organization_id>/', OrganizationDetailView.as_view(), name='organization-detail'),
    path('<int:organization_id>/invite-organizer/', InviteOrganizerView.as_view(), name='invite-organizer'),
    path('<int:organization_id>/event/<int:event_id>/distance/<int:distance_id>/user/',
         DistanceUserListView.as_view(), name='distance-user-list'),
    path('<int:organization_id>/event/<int:event_id>/distance/<int:distance_id>/user/<int:user_id>/',
         DistanceUserDetailView.as_view(), name='distance-user-detail')
]
