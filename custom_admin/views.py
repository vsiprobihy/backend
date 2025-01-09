from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.models import CustomUser
from authentication.permissions import IsAdmin
from custom_admin.models import OrganizerRequest
from custom_admin.serializers import OrganizerRequestSerializer, RequestStatusEventSerializer
from event.models import CompetitionType, Event
from event.serializers import CompetitionTypeSerializer, UpdateEventStatusSerializer
from swagger.custom_admin import SwaggerDocs
from utils.constants.constants_event import STATUS_PENDING
from utils.custom_exceptions import BadRequestError, ForbiddenError, NotFoundError, SuccessResponse
from utils.pagination import Pagination


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

        paginator = Pagination()
        paginator.page_size = 10
        paginated_requests = paginator.paginate_queryset(organizer_requests, request)

        if paginated_requests is not None:
            serializer = OrganizerRequestSerializer(paginated_requests, many=True)
            return paginator.get_paginated_response(serializer.data)

        serializer = OrganizerRequestSerializer(organizer_requests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateEventStatusView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    @swagger_auto_schema(**SwaggerDocs.UpdateEventStatusView.post)
    def post(self, request, event_id):
        serializer = UpdateEventStatusSerializer(data=request.data)

        if not serializer.is_valid():
            return BadRequestError('Status is not a valid choice.').get_response()

        event_status = serializer.validated_data.get('status')
        event = Event.objects.filter(id=event_id).first()

        if not event:
            return NotFoundError('Event not found.').get_response()

        if event.status == event_status:
            return (BadRequestError(
                f'The event status is already set to {event_status}. No changes were made.')
                    .get_response())

        event.status = event_status
        event.save()

        return SuccessResponse(f'Event status updated to {event_status}.').get_response()


class PendingEventsView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    @swagger_auto_schema(**SwaggerDocs.PendingEventsView.get)
    def get(self, request):
        events = Event.objects.filter(status=STATUS_PENDING)

        paginator = Pagination()
        paginator.page_size = 10
        paginated_events = paginator.paginate_queryset(events, request)

        if paginated_events is not None:
            serializer = RequestStatusEventSerializer(paginated_events, many=True)
            return paginator.get_paginated_response(serializer.data)

        serializer = RequestStatusEventSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CompetitionsTypeListCreateView(APIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsAdmin()]

    @swagger_auto_schema(**SwaggerDocs.CompetitionsTypeView.get)
    def get(self, request):
        competition_types = CompetitionType.objects.all().order_by('-id')

        paginator = Pagination()
        paginator.page_size = 12
        paginated_competition_types = paginator.paginate_queryset(competition_types, request)

        if paginated_competition_types is not None:
            serializer = CompetitionTypeSerializer(paginated_competition_types, many=True)
            return paginator.get_paginated_response(serializer.data)

        serializer = CompetitionTypeSerializer(competition_types, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(**SwaggerDocs.CompetitionsTypeView.post)
    def post(self, request):
        serializer = CompetitionTypeSerializer(data=request.data)

        if not serializer.is_valid():
            return BadRequestError('Invalid competition type data.').get_response()

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CompetitionsTypeDetailView(APIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsAdmin()]

    @swagger_auto_schema(**SwaggerDocs.CompetitionsTypeView.get)
    def get(self, request, competition_type_id):
        competition_type = CompetitionType.objects.filter(id=competition_type_id).first()

        if not competition_type:
            return NotFoundError('Competition type not found.').get_response()

        serializer = CompetitionTypeSerializer(competition_type)
        return Response(serializer.data)

    @swagger_auto_schema(**SwaggerDocs.CompetitionsTypeView.put)
    def put(self, request, competition_type_id):
        competition_type = CompetitionType.objects.filter(id=competition_type_id).first()

        if not competition_type:
            return NotFoundError('Competition type not found.').get_response()

        serializer = CompetitionTypeSerializer(competition_type, data=request.data, partial=True)

        if not serializer.is_valid():
            return BadRequestError('Invalid competition type data.').get_response()

        serializer.save()
        return Response(serializer.data)

    @swagger_auto_schema(**SwaggerDocs.CompetitionsTypeView.delete)
    def delete(self, request, competition_type_id):
        competition_type = CompetitionType.objects.filter(id=competition_type_id).first()

        if not competition_type:
            return NotFoundError('Competition type not found.').get_response()

        competition_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

