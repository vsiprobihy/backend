from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.models import CustomUser
from authentication.permissions import IsOrganizer
from event.additional_items.models import AdditionalItemEvent
from event.distance_details.models import DistanceEvent
from event.promo_code.models import PromoCode
from organization.decorators import (
    check_distance_access_decorator,
    check_organization_access_decorator,
    extract_event_directly,
)
from organization.models import Organization, Organizer
from organization.serializers import DistanceUserDetailSerializer, DistanceUserListSerializer, OrganizationSerializer
from swagger.organization import SwaggerDocs
from user.models import UserDistanceRegistration
from user.serializer import UserDistanceRegistrationSerializer
from utils.custom_exceptions import BadRequestError, ForbiddenError, NotFoundError, SuccessResponse
from utils.pagination import Pagination


User = get_user_model()


class OrganizationListCreateView(APIView):
    permission_classes = [IsAuthenticated, IsOrganizer]

    @swagger_auto_schema(**SwaggerDocs.Organization.get)
    def get(self, request):
        organization = Organization.objects.filter(organizerOrganization__user=request.user)

        paginator = Pagination()
        paginator.page_size = 4

        paginated_organizations = paginator.paginate_queryset(organization, request)

        if paginated_organizations is not None:
            serializer = OrganizationSerializer(paginated_organizations, many=True, context={'request': request})
            return paginator.get_paginated_response(serializer.data)

        serializer = OrganizationSerializer(organization, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(**SwaggerDocs.Organization.post)
    def post(self, request):
        serializer = OrganizationSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            organization = serializer.save()
            Organizer.objects.create(
                user=request.user,
                organization=organization,
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrganizationDetailView(APIView):
    permission_classes = [IsAuthenticated, IsOrganizer]

    @swagger_auto_schema(**SwaggerDocs.Organization.get)
    def get(self, request, organization_id):
        organization = Organization.objects.filter(
            organizerOrganization__user=request.user, pk=organization_id
        ).first()  # noqa: E501
        if organization:
            serializer = OrganizationSerializer(organization, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        return ForbiddenError('You dont have permission to this action').get_response()

    @swagger_auto_schema(**SwaggerDocs.Organization.put)
    def put(self, request, organization_id):
        organization = Organization.objects.filter(
            organizerOrganization__user=request.user, pk=organization_id
        ).first()  # noqa: E501
        if not organization:
            return ForbiddenError('You dont have permission to this action').get_response()

        serializer = OrganizationSerializer(organization, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(**SwaggerDocs.Organization.patch)
    def patch(self, request, organization_id):
        organization = Organization.objects.filter(
            organizerOrganization__user=request.user, pk=organization_id
        ).first()  # noqa: E501
        if not organization:
            return ForbiddenError('You dont have permission to this action').get_response()

        serializer = OrganizationSerializer(organization, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(**SwaggerDocs.Organization.delete)
    def delete(self, request, organization_id):
        organization = Organization.objects.filter(organizerOrganization__user=request.user, pk=organization_id).first()

        if organization is None:
            return NotFoundError('User not found.').get_response()

        organization.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class InviteOrganizerView(APIView):
    permission_classes = [IsAuthenticated, IsOrganizer]

    @swagger_auto_schema(**SwaggerDocs.InviteOrganizer.post)
    def post(self, request, organization_id):
        email = request.data.get('email')
        message = request.data.get('message', '')  # noqa: F841

        user = User.objects.filter(email=email).first()
        if not user:
            return NotFoundError('User with this email not found').get_response()

        organization = Organization.objects.filter(pk=organization_id).first()
        if not organization:
            return NotFoundError('User with this email not found').get_response()

        is_organizer = Organizer.objects.filter(
            organization=organization, user=request.user, role=CustomUser.ORGANIZER
        ).exists()
        if not is_organizer:
            return ForbiddenError('You are not the organizer of this organization').get_response()

        Organizer.objects.create(user=user, organization=organization, role=CustomUser.ORGANIZER)

        return SuccessResponse('Organizer invited successfully').get_response()


class DistanceUserListView(APIView):
    permission_classes = [IsAuthenticated, IsOrganizer]

    @swagger_auto_schema(**SwaggerDocs.OrganizationDistanceUserList.get)
    @check_organization_access_decorator(extract_event_directly)
    @check_distance_access_decorator()
    def get(self, request, organization_id, event_id, distance_id):
        registrations = (
            UserDistanceRegistration.objects.filter(distance_id=distance_id)
            .prefetch_related('additionalItems')
            .order_by('id')
        )

        paginator = Pagination()
        paginator.page_size = 4

        paginated_organizations = paginator.paginate_queryset(registrations, request)

        if paginated_organizations is not None:
            serializer = DistanceUserListSerializer(paginated_organizations, many=True)
            return paginator.get_paginated_response(serializer.data)

        serializer = DistanceUserListSerializer(registrations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DistanceUserDetailView(APIView):
    permission_classes = [IsAuthenticated, IsOrganizer]

    @swagger_auto_schema(**SwaggerDocs.OrganizationDistanceUser.get)
    @check_organization_access_decorator(extract_event_directly)
    @check_distance_access_decorator()
    def get(self, request, organization_id, event_id, distance_id, user_id):
        registration = UserDistanceRegistration.objects.filter(distance_id=distance_id, user_id=user_id).first()

        if registration is None:
            return NotFoundError('User not found.').get_response()

        serializer = DistanceUserDetailSerializer(registration)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(**SwaggerDocs.OrganizationDistanceUser.post)
    @check_organization_access_decorator(extract_event_directly)
    @check_distance_access_decorator()
    def post(self, request, organization_id, event_id, distance_id, user_id):
        user = CustomUser.objects.get(id=user_id)
        distance = DistanceEvent.objects.filter(id=distance_id).first()

        if not distance:
            return NotFoundError('Distance not found.').get_response()

        event = distance.event
        if event.status != 'published':
            return BadRequestError('The event must be published to register.').get_response()

        if UserDistanceRegistration.objects.filter(user=user, distance=distance).exists():
            return BadRequestError('You are already registered for this distance.').get_response()

        assigned_numbers = (
            UserDistanceRegistration.objects.filter(distance=distance)
            .values_list('startingNumber', flat=True)
        )
        available_numbers = set(range(distance.startNumberFrom, distance.startNumberTo + 1)) - set(assigned_numbers)
        if not available_numbers:
            return BadRequestError('No available starting numbers for this distance.').get_response()

        starting_number = min(available_numbers)

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
            registration = serializer.save(
                user=user,
                distance=distance,
                promoCode=promo_code,
                startingNumber=starting_number
            )
            registration.additionalItems.set(additional_items)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return BadRequestError(serializer.errors).get_response()

    @swagger_auto_schema(**SwaggerDocs.OrganizationDistanceUser.put)
    @check_organization_access_decorator(extract_event_directly)
    @check_distance_access_decorator()
    def put(self, request, organization_id, event_id, distance_id, user_id):
        registration = UserDistanceRegistration.objects.filter(distance_id=distance_id, user_id=user_id).first()
        if registration is None:
            return NotFoundError('User not found.').get_response()

        serializer = DistanceUserDetailSerializer(registration, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(**SwaggerDocs.OrganizationDistanceUser.patch)
    @check_organization_access_decorator(extract_event_directly)
    @check_distance_access_decorator()
    def patch(self, request, organization_id, event_id, distance_id, user_id):
        registration = UserDistanceRegistration.objects.filter(distance_id=distance_id, user_id=user_id).first()
        if registration is None:
            return NotFoundError('User not found.').get_response()

        serializer = DistanceUserDetailSerializer(
            registration, data=request.data, partial=True, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(**SwaggerDocs.OrganizationDistanceUser.delete)
    @check_organization_access_decorator(extract_event_directly)
    @check_distance_access_decorator()
    def delete(self, request, organization_id, event_id, distance_id, user_id):
        registration = UserDistanceRegistration.objects.filter(distance_id=distance_id, user_id=user_id).first()

        if registration is None:
            return NotFoundError('User not found.').get_response()

        registration.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
