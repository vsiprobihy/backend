from django.urls import path

from public_event.views import PublicEventDetailView, PublicEventFilterView, PublicEventListView


urlpatterns = [
    path('', PublicEventListView.as_view(), name='public-event-list'),
    path('<int:event_id>/', PublicEventDetailView.as_view(), name='public-event-detail'),
    path('filter/', PublicEventFilterView.as_view(), name='public-event-filter'),
]
