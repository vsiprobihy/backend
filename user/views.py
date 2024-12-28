from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.models import AdditionalProfile, CustomUser
from authentication.serializers import (
    AdditionalProfileDetailSerializer,
    AdditionalProfileSerializer,
    UserProfileSerializer,
)
from custom_admin.models import OrganizerRequest
from event.additional_items.models import AdditionalItemEvent
from event.distance_details.models import DistanceEvent
from event.models import Event
from event.promo_code.models import PromoCode
from swagger.user import SwaggerDocs
from user.models import EventLike, UserDistanceRegistration
from user.serializer import UserDistanceRegistrationSerializer
from utils.constants.constants_event import STATUS_PENDING, STATUS_UNPUBLISHED
from utils.custom_exceptions import BadRequestError, CreatedResponse, ForbiddenError, NotFoundError


class UserDistanceRegistrationView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(**SwaggerDocs.UserDistanceRegistrationView.post)
    def post(self, request, distance_id):
        user = request.user
        distance = DistanceEvent.objects.filter(id=distance_id).first()

        if not distance:
            return NotFoundError('Distance not found.').get_response()

        if UserDistanceRegistration.objects.filter(user=user, distance=distance).exists():
            return BadRequestError('You are already registered for this distance.').get_response()

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
        profiles = request.user.additional_profiles.all()
        serializer = AdditionalProfileSerializer(profiles, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(**SwaggerDocs.AdditionalProfileList.post)
    def post(self, request):
        serializer = AdditionalProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdditionalProfileDetailView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(**SwaggerDocs.AdditionalProfileDetail.get)
    def get(self, request, _id):
        try:
            profile = request.user.additional_profiles.get(id=_id)
            serializer = AdditionalProfileDetailSerializer(profile)
            return Response(serializer.data)
        except AdditionalProfile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(**SwaggerDocs.AdditionalProfileDetail.put)
    def put(self, request, _id):
        try:
            profile = request.user.additional_profiles.get(id=_id)
            serializer = AdditionalProfileDetailSerializer(profile, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except AdditionalProfile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(**SwaggerDocs.AdditionalProfileDetail.delete)
    def delete(self, request, _id):
        try:
            profile = request.user.additional_profiles.get(id=_id)
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
            EventLike.objects.like_event(request.user, event)
            return Response({'detail': 'Event liked successfully'}, status=status.HTTP_200_OK)
        except Event.DoesNotExist:
            return Response({'detail': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(**SwaggerDocs.LikeEventView.delete)
    def delete(self, request, event_id):
        try:
            event = Event.objects.get(id=event_id)
            EventLike.objects.unlike_event(request.user, event)
            return Response({'detail': 'Event unliked successfully'}, status=status.HTTP_200_OK)
        except Event.DoesNotExist:
            return Response({'detail': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)


class LikedEventsView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(**SwaggerDocs.LikedEventsView.get)
    def get(self, request):
        liked_events = EventLike.objects.get_liked_events(request.user)
        data = [
            {'id': event.id, 'name': event.name, 'dateFrom': event.dateFrom, 'dateTo': event.dateTo}
            for event in liked_events
        ]
        return Response(data, status=status.HTTP_200_OK)
