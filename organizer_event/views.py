from datetime import datetime

from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.permissions import IsOrganizer
from organization.decorators import check_organization_access_decorator, extract_for_event_access_directly
from organization.models import OrganizationAccess
from organizer_event.models import Event
from organizer_event.serializers import EventSerializer
from swagger.event import SwaggerDocs
from utils.pagination import Pagination


class EventsListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsOrganizer]

    @swagger_auto_schema(**SwaggerDocs.EventsListCreateView.get)
    def get(self, request):
        current_date = datetime.now().date()
        archives = request.GET.get('archives', None)

        organizer_access = OrganizationAccess.objects.filter(user=request.user)
        organizer_ids = organizer_access.values_list('organization__id', flat=True)

        if archives:
            events = (Event.objects.filter(organizer__id__in=organizer_ids)
                      .order_by('-date_from')
                      .filter(date_to__lt=current_date)
                      )
        else:
            events = (Event.objects.filter(organizer__id__in=organizer_ids)
                      .order_by('-date_from')
                      )

        paginator = Pagination()
        paginator.page_size = 6  # temporary long value

        paginated_events = paginator.paginate_queryset(events, request)

        if paginated_events is not None:
            serializer = EventSerializer(paginated_events, many=True)
            return paginator.get_paginated_response(serializer.data)

        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(**SwaggerDocs.EventsListCreateView.post)
    def post(self, request):
        serializer = EventSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsOrganizer]

    def get_object(self, event_id):
        event = Event.objects.get(pk=event_id)
        return event

    @swagger_auto_schema(**SwaggerDocs.EventDetailView.get)
    @check_organization_access_decorator(extract_for_event_access_directly)
    def get(self, request, organizer_id, event_id):
        event = self.get_object(event_id)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    @swagger_auto_schema(**SwaggerDocs.EventDetailView.put)
    @check_organization_access_decorator(extract_for_event_access_directly)
    def put(self, request, organizer_id, event_id):
        event = self.get_object(event_id)
        request.data['organizer_id'] = organizer_id
        serializer = EventSerializer(event, data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(**SwaggerDocs.EventDetailView.patch)
    @check_organization_access_decorator(extract_for_event_access_directly)
    def patch(self, request, organizer_id, event_id):
        event = self.get_object(event_id)
        serializer = EventSerializer(event, data=request.data, partial=True, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(**SwaggerDocs.EventDetailView.delete)
    @check_organization_access_decorator(extract_for_event_access_directly)
    def delete(self, request, organizer_id, event_id):
        event = self.get_object(event_id)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

