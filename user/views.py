from django.utils.timezone import now
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.models import CustomUser
from authentication.serializers import (
    UserProfileSerializer,
)
from custom_admin.models import OrganizerRequest
from event.additional_items.models import AdditionalItemEvent
from event.distance_details.models import DistanceEvent
from event.models import Event
from event.promo_code.models import PromoCode
from swagger.user import SwaggerDocs
from user.models import AdditionalProfile, EventLike, UserDistanceRegistration
from user.serializer import (
    AdditionalProfileSerializer,
    UserDistanceRegistrationSerializer,
)
from utils.constants.constants_event import STATUS_PENDING, STATUS_UNPUBLISHED
from utils.custom_exceptions import BadRequestError, CreatedResponse, ForbiddenError, NotFoundError
from utils.pagination import Pagination


class UserDistanceRegistrationView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(**SwaggerDocs.UserDistanceRegistrationView.post)
    def post(self, request, distance_id):
        user = request.user
        distance = DistanceEvent.objects.filter(id=distance_id).first()

        if not distance:
            return NotFoundError('Distance not found.').get_response()

        event = distance.event
        if event.status != 'published':
            return BadRequestError('The event must be published to register.').get_response()

        if UserDistanceRegistration.objects.filter(user=user, distance=distance).exists():
            return BadRequestError('You are already registered for this distance.').get_response()

        # TODO: Add startingNumber
        # startingNumber

        promo_code_id = request.data.get('promoCode')
        promo_code = None
        if promo_code_id:
            promo_code = PromoCode.objects.filter(id=promo_code_id, isActive=True, distance=distance).first()
            if not promo_code:
                return BadRequestError('Invalid promo code.').get_response()

        additional_item_ids = request.data.get('additionalItems', [])
        additional_items = AdditionalItemEvent.objects.filter(id__in=additional_item_ids, distance=distance)

        if len(additional_item_ids) != additional_items.count():
            return BadRequestError('One or more additional items are invalid.').get_response()

        serializer = UserDistanceRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            registration = serializer.save(user=user, distance=distance, promoCode=promo_code)
            registration.additionalItems.set(additional_items)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return BadRequestError(serializer.errors).get_response()


class UserDistanceRegistrationsView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(**SwaggerDocs.UserDistanceRegistrationView.get)
    def get(self, request):
        status_filter = request.query_params.get('status')
        registrations = UserDistanceRegistration.objects.filter(user=request.user)

        if status_filter == 'active':
            registrations = registrations.filter(distance__event__dateTo__gte=now().date())
        elif status_filter == 'archive':
            registrations = registrations.filter(distance__event__dateTo__lt=now().date())

        paginator = Pagination()
        paginator.page_size = 4

        paginated_registrations = paginator.paginate_queryset(registrations, request)

        if paginated_registrations is not None:
            serializer = UserDistanceRegistrationSerializer(paginated_registrations, many=True)
            return paginator.get_paginated_response(serializer.data)

        serializer = UserDistanceRegistrationSerializer(registrations, many=True)

        return Response(serializer.data)


class RequestOrganizerView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(**SwaggerDocs.RequestOrganizerView.post)
    def post(self, request):
        user = request.user

        if user.role != CustomUser.USER:
            return ForbiddenError('You do not have permission to perform this action.').get_response()

        if OrganizerRequest.objects.filter(user=user, isApproved=False).exists():
            return BadRequestError('You already have a pending request.').get_response()

        OrganizerRequest.objects.create(user=user)
        return CreatedResponse('Request submitted successfully.').get_response()


class AdditionalProfileListView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(**SwaggerDocs.AdditionalProfileList.get)
    def get(self, request):
        profiles = request.user.additionalProfiles.all()

        paginator = Pagination()
        paginated_profiles = paginator.paginate_queryset(profiles, request)

        if paginated_profiles is not None:
            serializer = AdditionalProfileSerializer(paginated_profiles, many=True)
            return paginator.get_paginated_response(serializer.data)

        serializer = AdditionalProfileSerializer(profiles, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(**SwaggerDocs.AdditionalProfileList.post)
    def post(self, request):
        serializer = AdditionalProfileSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdditionalProfileDetailView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(**SwaggerDocs.AdditionalProfileDetail.get)
    def get(self, request, profile_id):
        try:
            profile = request.user.additionalProfiles.get(id=profile_id)
            serializer = AdditionalProfileSerializer(profile)
            return Response(serializer.data)
        except AdditionalProfile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(**SwaggerDocs.AdditionalProfileDetail.put)
    def put(self, request, profile_id):
        try:
            profile = request.user.additionalProfiles.get(id=profile_id)
            serializer = AdditionalProfileSerializer(
                profile, data=request.data, context={'request': request}
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except AdditionalProfile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(**SwaggerDocs.AdditionalProfileDetail.patch)
    def patch(self, request, profile_id):
        try:
            profile = request.user.additionalProfiles.get(id=profile_id)
            serializer = AdditionalProfileSerializer(
                profile, data=request.data, partial=True, context={'request': request}
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except AdditionalProfile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(**SwaggerDocs.AdditionalProfileDetail.delete)
    def delete(self, request, profile_id):
        try:
            profile = request.user.additionalProfiles.get(id=profile_id)
            profile.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except AdditionalProfile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(**SwaggerDocs.Profile.get)
    def get(self, request):
        user = request.user
        serializer = UserProfileSerializer(user, context={'request': request})
        return Response(serializer.data)

    @swagger_auto_schema(**SwaggerDocs.Profile.put)
    def put(self, request):
        user = request.user
        serializer = UserProfileSerializer(user, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(**SwaggerDocs.Profile.patch)
    def patch(self, request):
        user = request.user
        serializer = UserProfileSerializer(user, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LikeEventView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(**SwaggerDocs.LikeEventView.post)
    def post(self, request, event_id):
        try:
            event = Event.objects.get(id=event_id)
            if event.status in [STATUS_PENDING, STATUS_UNPUBLISHED]:
                return Response(
                    {'detail': 'Event is not available for liking.'},
                    status=status.HTTP_403_FORBIDDEN,
                )

            if EventLike.objects.filter(user=request.user, event=event).exists():
                return Response({'detail': 'Event already liked.'}, status=status.HTTP_400_BAD_REQUEST)

            EventLike.objects.like_event(request.user, event)
            return Response({'detail': 'Event liked successfully'}, status=status.HTTP_200_OK)
        except Event.DoesNotExist:
            return Response({'detail': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(**SwaggerDocs.LikeEventView.delete)
    def delete(self, request, event_id):
        try:
            event = Event.objects.get(id=event_id)

            if not EventLike.objects.filter(user=request.user, event=event).exists():
                return Response({'detail': 'Event already unliked.'}, status=status.HTTP_400_BAD_REQUEST)

            EventLike.objects.unlike_event(request.user, event)
            return Response({'detail': 'Event unliked successfully'}, status=status.HTTP_200_OK)
        except Event.DoesNotExist:
            return Response({'detail': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)


class LikedEventsView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(**SwaggerDocs.LikedEventsView.get)
    def get(self, request):
        liked_events = EventLike.objects.get_liked_events(request.user)

        paginator = Pagination()
        paginator.page_size = 4

        paginated_events = paginator.paginate_queryset(liked_events, request)

        if paginated_events:
            data = [
                {'id': event.id, 'name': event.name, 'dateFrom': event.dateFrom, 'dateTo': event.dateTo}
                for event in paginated_events
            ]
            return paginator.get_paginated_response(data)

        return paginator.get_paginated_response([])
