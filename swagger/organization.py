from drf_yasg import openapi

from organization.serializers import DistanceUserDetailSerializer, DistanceUserListSerializer, OrganizationSerializer
from swagger.organization_variables import Request


class SwaggerDocs:

    class Organization:
        get = {
            'tags': ['Organization'],
            'operation_description': 'Retrieve a list of organizations with pagination.',
            'responses': {
                200: openapi.Response(
                    description='List of organizations with pagination',
                    schema=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'pagination': openapi.Schema(
                                type=openapi.TYPE_OBJECT,
                                properties={
                                    'next_page': openapi.Schema(
                                        type=openapi.TYPE_STRING,
                                        description='URL for the next page of results',
                                        nullable=True
                                    ),
                                    'current_page': openapi.Schema(
                                        type=openapi.TYPE_INTEGER,
                                        description='Current page number'
                                    ),
                                    'previous_page': openapi.Schema(
                                        type=openapi.TYPE_STRING,
                                        description='URL for the previous page of results',
                                        nullable=True
                                    ),
                                    'num_pages': openapi.Schema(
                                        type=openapi.TYPE_INTEGER,
                                        description='Total number of pages'
                                    ),
                                },
                                required=['next_page', 'current_page', 'num_pages']
                            ),
                            'items_count': openapi.Schema(
                                type=openapi.TYPE_INTEGER,
                                description='Total number of organizations'
                            ),
                            'items': openapi.Schema(
                                type=openapi.TYPE_ARRAY,
                                items=openapi.Items(
                                    type=openapi.TYPE_OBJECT,
                                    properties={
                                        'id': openapi.Schema(
                                            type=openapi.TYPE_INTEGER,
                                            description='ID of the organization'
                                        ),
                                        'users': openapi.Schema(
                                            type=openapi.TYPE_ARRAY,
                                            items=openapi.Items(
                                                type=openapi.TYPE_OBJECT,
                                                properties={
                                                    'user': openapi.Schema(
                                                        type=openapi.TYPE_STRING,
                                                        description='Email of the user'
                                                    ),
                                                    'role': openapi.Schema(
                                                        type=openapi.TYPE_STRING,
                                                        description='Role of the user in the organization'
                                                    ),
                                                },
                                                required=['user', 'role']
                                            )
                                        ),
                                        'phoneNumbers': openapi.Schema(
                                            type=openapi.TYPE_ARRAY,
                                            items=openapi.Items(type=openapi.TYPE_STRING),
                                            description='List of phone numbers for the organization'
                                        ),
                                        'name': openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description='Name of the organization'
                                        ),
                                        'siteUrl': openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description='URL of the organization website',
                                            nullable=True
                                        ),
                                        'email': openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description='Email of the organization'
                                        ),
                                        'instagramUrl': openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description='Instagram URL of the organization',
                                            nullable=True
                                        ),
                                        'facebookUrl': openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description='Facebook URL of the organization',
                                            nullable=True
                                        ),
                                        'telegramUrl': openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description='Telegram URL of the organization',
                                            nullable=True
                                        ),
                                        'mainImage': openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description='Main image of the organization',
                                            nullable=True
                                        ),
                                        'backgroundImage': openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description='Background image of the organization',
                                            nullable=True
                                        ),
                                    },
                                    required=['id', 'users', 'phoneNumbers', 'name', 'email']
                                )
                            ),
                        },
                        required=['pagination', 'items_count', 'items']
                    )
                ),
                401: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Authentication credentials were not provided.'
                        )
                    },
                    required=['detail'],
                ),
                403: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='You do not have permission to perform this action.'
                        )
                    },
                    required=['detail'],
                ),
                404: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Organization not found.'
                        )
                    },
                    required=['detail'],
                ),
                500: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='An unexpected error occurred on the server.'
                        )
                    },
                    required=['detail'],
                ),
            },
        }


        post = {
            'tags': ['Organization'],
            'request_body': OrganizationSerializer,
            'responses': {
                200: openapi.Response('Updated organizer', OrganizationSerializer),
                401: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING, description='Authentication credentials were not provided.'
                        )
                    },
                    required=['detail'],
                ),
                403: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='You do not have permission to perform this action.',
                        )
                    },
                    required=['detail'],
                ),
                500: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='An unexpected error occurred on the server.',
                        )
                    },
                    required=['detail'],
                ),
            },
            'operation_description': 'Update the details of an event organizer by event_id. The event_id is used to find the organizer, and the request body contains the updated information about the organizer.',  # noqa: E501
        }

        put = {
            'tags': ['Organization'],
            'request_body': OrganizationSerializer,
            'responses': {
                200: openapi.Response('Updated organizer', OrganizationSerializer),
                401: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING, description='Authentication credentials were not provided.'
                        )
                    },
                    required=['detail'],
                ),
                403: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='You do not have permission to perform this action.',
                        )
                    },
                    required=['detail'],
                ),
                404: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING, description='Organization not found.'
                        )
                    },
                    required=['detail'],
                ),
                500: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='An unexpected error occurred on the server.',
                        )
                    },
                    required=['detail'],
                ),
            },
            'operation_description': 'Update the details of an event organizer by event_id. The event_id is used to find the organizer, and the request body contains the updated information about the organizer.',  # noqa: E501
        }

        patch = {
            'tags': ['Organization'],
            'request_body': OrganizationSerializer,
            'responses': {
                200: openapi.Response(
                    'Partially updated organizer', OrganizationSerializer
                ),
                401: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING, description='Authentication credentials were not provided.'
                        )
                    },
                    required=['detail'],
                ),
                403: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='You do not have permission to perform this action.',
                        )
                    },
                    required=['detail'],
                ),
                404: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING, description='Organization not found.'
                        )
                    },
                    required=['detail'],
                ),
                500: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='An unexpected error occurred on the server.',
                        )
                    },
                    required=['detail'],
                ),
            },
            'operation_description': 'Partially update an event organizer by event_id. Only the fields provided in the request body will be updated.',  # noqa: E501
        }

        delete = {
            'tags': ['Organization'],
            'responses': {
                204: 'Organizer deleted successfully',
                401: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING, description='Authentication credentials were not provided.'
                        )
                    },
                    required=['detail'],
                ),
                403: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='You do not have permission to perform this action.',
                        )
                    },
                    required=['detail'],
                ),
                404: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING, description='Organization not found.'
                        )
                    },
                    required=['detail'],
                ),
                500: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='An unexpected error occurred on the server.',
                        )
                    },
                    required=['detail'],
                ),
            },
            'operation_description': 'Delete an event organizer by event_id. The event_id is used to find and delete the organizer associated with a specific event.',  # noqa: E501
        }

    class OrganizationDistanceUser:
        get = {
            'tags': ['Organization Distance User'],
            'responses': {
                200: openapi.Response('Success', DistanceUserDetailSerializer),
                401: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING, description='Authentication credentials were not provided.'
                        )
                    },
                    required=['detail'],
                ),
                403: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='You do not have permission to perform this action.',
                        )
                    },
                    required=['detail'],
                ),
                404: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Not found.',
                            enum=[
                                'Not found.',
                                'User not found.',
                                'Event not found.',
                                'Distance not found.',
                                'Organization not found.',
                            ]
                        )
                    },
                    required=['detail'],
                ),
                500: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='An unexpected error occurred on the server.',
                        )
                    },
                    required=['detail'],
                ),
            },
            'operation_description': 'Retrieve the users',  # noqa: E501
        }

        put = {
            'tags': ['Organization Distance User'],
            'request_body': DistanceUserDetailSerializer,
            'responses': {
                200: openapi.Response('Success', DistanceUserDetailSerializer),
                401: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING, description='Authentication credentials were not provided.'
                        )
                    },
                    required=['detail'],
                ),
                403: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='You do not have permission to perform this action.',
                        )
                    },
                    required=['detail'],
                ),
                404: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Not found.',
                            enum=[
                                'Not found.',
                                'User not found.',
                                'Event not found.',
                                'Distance not found.',
                                'Organization not found.',
                            ]
                        )
                    },
                    required=['detail'],
                ),
                500: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='An unexpected error occurred on the server.',
                        )
                    },
                    required=['detail'],
                ),
            },
            'operation_description': 'Update the details of user',  # noqa: E501
        }

        patch = {
            'tags': ['Organization Distance User'],
            'request_body': DistanceUserDetailSerializer,
            'responses': {
                200: openapi.Response('Success', DistanceUserDetailSerializer),
                401: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING, description='Authentication credentials were not provided.'
                        )
                    },
                    required=['detail'],
                ),
                403: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='You do not have permission to perform this action.',
                        )
                    },
                    required=['detail'],
                ),
                404: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Not found.',
                            enum=[
                                'Not found.',
                                'User not found.',
                                'Event not found.',
                                'Distance not found.',
                                'Organization not found.',
                            ]
                        )
                    },
                    required=['detail'],
                ),
                500: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='An unexpected error occurred on the server.',
                        )
                    },
                    required=['detail'],
                ),
            },
            'operation_description': 'Partially update an user by user_id. Only the fields provided in the request body will be updated.',  # noqa: E501
        }

        delete = {
            'tags': ['Organization Distance User'],
            'responses': {
                204: 'Organizer deleted successfully',
                401: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING, description='Authentication credentials were not provided.'
                        )
                    },
                    required=['detail'],
                ),
                403: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='You do not have permission to perform this action.',
                        )
                    },
                    required=['detail'],
                ),
                404: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Not found.',
                            enum=[
                                'Not found.',
                                'User not found.',
                                'Event not found.',
                                'Distance not found.',
                                'Organization not found.',
                            ]
                        )
                    },
                    required=['detail'],
                ),
                500: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='An unexpected error occurred on the server.',
                        )
                    },
                    required=['detail'],
                ),
            },
            'operation_description': 'Delete an event organizer by event_id. The event_id is used to find and delete the organizer associated with a specific event.',  # noqa: E501
        }

    class OrganizationDistanceUserList:
        get = {
            'tags': ['Organization Distance User'],
            'responses': {
                200: openapi.Response('Success', DistanceUserListSerializer),
                401: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING, description='Authentication credentials were not provided.'
                        )
                    },
                    required=['detail'],
                ),
                403: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='You do not have permission to perform this action.',
                        )
                    },
                    required=['detail'],
                ),
                404: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Not found.',
                            enum=[
                                'Not found.',
                                'User not found.',
                                'Event not found.',
                                'Distance not found.',
                                'Organization not found.',
                            ]
                        )
                    },
                    required=['detail'],
                ),
                500: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='An unexpected error occurred on the server.',
                        )
                    },
                    required=['detail'],
                ),
            },
            'operation_description': 'Retrieve the list of users',  # noqa: E501
        }

    class InviteOrganizer:
        post = {
            'tags': ['Organization'],
            'request_body': Request.ModeratorInviteRequestBody,
            'responses': {
                200: 'Invite sent successfully',
                404: 'Organizer not found',
            },
            'operation_description': 'Send an invitation to an organizer by email. The email address of the organizer is provided in the request body.',  # noqa: E501
        }
