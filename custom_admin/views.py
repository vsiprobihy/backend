from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from authentication.models import CustomUser
from authentication.permissions import IsAdmin
from custom_admin.models import OrganizerRequest
from custom_admin.serializers import OrganizerRequestSerializer, RequestStatusEventSerializer
from event.models import CompetitionType, Event
from event.serializers import CompetitionTypeSerializer, UpdateEventStatusSerializer
from swagger.custom_admin import SwaggerDocs
from utils.constants.constants_event import STATUS_PENDING
from utils.custom_exceptions import BadRequestError, ForbiddenError, NotFoundError, SuccessResponse


class ApproveOrganizerView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    @swagger_auto_schema(**SwaggerDocs.ApproveOrganizerView.post)
    def post(self, request, user_id):
        if not request.user.is_superuser:
            return ForbiddenError('You do not have permission to perform this action.').get_response()

        organizer_request = OrganizerRequest.objects.filter(user_id=user_id, isApproved=False).first()
        if not organizer_request:
            return NotFoundError('Request not found.').get_response()

        organizer_request.isApproved = True
        organizer_request.save()

        user = organizer_request.user
        user.role = CustomUser.ORGANIZER
        user.save()

        return SuccessResponse('Request approved and user is now an organizer.').get_response()


class OrganizerRequestsListView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    @swagger_auto_schema(**SwaggerDocs.OrganizerRequestsListView.get)
    def get(self, request):
        if not request.user.is_superuser:
            return ForbiddenError('You do not have permission to perform this action.').get_response()

        organizer_requests = OrganizerRequest.objects.filter(isApproved=False)
        serializer = OrganizerRequestSerializer(organizer_requests, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)



class CompetitionsTypeViewSet(ModelViewSet):
    queryset = CompetitionType.objects.all()
    serializer_class = CompetitionTypeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(**SwaggerDocs.CompetitionsTypeViewSet.get)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(**SwaggerDocs.CompetitionsTypeViewSet.get)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(**SwaggerDocs.CompetitionsTypeViewSet.post)
    def create(self, request, *args, **kwargs):
        self.check_permissions(request)
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(**SwaggerDocs.CompetitionsTypeViewSet.put)
    def update(self, request, *args, **kwargs):
        self.check_permissions(request)
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(**SwaggerDocs.CompetitionsTypeViewSet.patch)
    def partial_update(self, request, *args, **kwargs):
        self.check_permissions(request)
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(**SwaggerDocs.CompetitionsTypeViewSet.delete)
    def destroy(self, request, *args, **kwargs):
        self.check_permissions(request)
        return super().destroy(request, *args, **kwargs)

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticatedOrReadOnly()]
        return [IsAdmin()]

class UpdateEventStatusView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    @swagger_auto_schema(**SwaggerDocs.UpdateEventStatusView.post)
    def post(self, request, event_id):
        serializer = UpdateEventStatusSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        event_status = serializer.validated_data.get('status')
        event = Event.objects.filter(id=event_id).first()

        if not event:
            return BadRequestError('Event not found.').get_response()

        event.status = event_status
        event.save()

        return SuccessResponse(f'Event status updated to {event_status}.').get_response()


class PendingEventsView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    @swagger_auto_schema(**SwaggerDocs.PendingEventsView.get)
    def get(self, request):
        events = Event.objects.filter(status=STATUS_PENDING)
        serializer = RequestStatusEventSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
