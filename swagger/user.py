from drf_yasg import openapi

from authentication.serializers import (
    UserProfileSerializer,
)
from user.serializer import (
    AdditionalProfileSerializer,
    UserDistanceRegistrationSerializer,
)


class SwaggerDocs:
    class RequestOrganizerView:
        post = {
            'tags': ['Request Organizer'],
            'operation_description': 'Request Organizer',
            'responses': {
                200: 'Request submitted successfully.',
                400: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING, description='You already have a pending request.'
                        )
                    },
                    required=['detail'],
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
                            type=openapi.TYPE_STRING, description='Request not found.'
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
        }

    class UserDistanceRegistrationView:
        get = {
            'tags': ['User Distance Registration'],
            'operation_description': (
                'Get all registrations of the authenticated user. Use "status" query parameter to filter:\n'
                '- "active" for active registrations\n'
                '- "archive" for archived registrations'
            ),
            'manual_parameters': [
                openapi.Parameter(
                    'status',
                    openapi.IN_QUERY,
                    description='Filter by status: "active" or "archive".',
                    type=openapi.TYPE_STRING,
                    enum=['active', 'archive'],
                ),
                openapi.Parameter(
                    'page', openapi.IN_QUERY, description='Page number for pagination', type=openapi.TYPE_STRING
                ),
            ],
            'responses': {
                200: openapi.Response(
                    description='List of user registrations',
                    schema=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'pagination': openapi.Schema(
                                type=openapi.TYPE_OBJECT,
                                properties={
                                    'next_page': openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
                                    'current_page': openapi.Schema(type=openapi.TYPE_INTEGER),
                                    'previous_page': openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
                                    'num_pages': openapi.Schema(type=openapi.TYPE_INTEGER),
                                },
                                required=['current_page', 'num_pages'],
                            ),
                            'items_count': openapi.Schema(type=openapi.TYPE_INTEGER, description='Total item count'),
                            'items': openapi.Schema(
                                type=openapi.TYPE_ARRAY,
                                items=openapi.Schema(
                                    type=openapi.TYPE_OBJECT,
                                    properties={
                                        'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='User ID'),
                                        'registrationDate': openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            format='date-time',
                                            description='Date of registration'
                                        ),
                                        'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email'),
                                        'firstName': openapi.Schema(type=openapi.TYPE_STRING, description='First name'),
                                        'lastName': openapi.Schema(type=openapi.TYPE_STRING, description='Last name'),
                                        'firstNameEng': openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description='First name in English'
                                        ),
                                        'lastNameEng': openapi.Schema(
                                            type=openapi.TYPE_STRING, description='Last name in English'
                                        ),
                                        'gender': openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            enum=['M', 'F'],
                                            description='Gender'
                                        ),
                                        'dateOfBirth': openapi.Schema(
                                            type=openapi.TYPE_STRING, format='date', description='Date of birth'
                                        ),
                                        'tShirtSize': openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description='T-shirt size'
                                        ),
                                        'country': openapi.Schema(type=openapi.TYPE_STRING, description='Country'),
                                        'city': openapi.Schema(type=openapi.TYPE_STRING, description='City'),
                                        'phoneNumber': openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description='Phone number'
                                        ),
                                        'sportsClub': openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description='Sports club'
                                        ),
                                        'emergencyContactName': openapi.Schema(
                                            type=openapi.TYPE_STRING, description='Emergency contact name'
                                        ),
                                        'emergencyContactPhone': openapi.Schema(
                                            type=openapi.TYPE_STRING, description='Emergency contact phone'
                                        ),
                                        'promoCode': openapi.Schema(
                                            type=openapi.TYPE_STRING, description='Promo code', nullable=True
                                        ),
                                        'additionalItems': openapi.Schema(
                                            type=openapi.TYPE_ARRAY,
                                            items=openapi.Schema(
                                                type=openapi.TYPE_OBJECT,
                                                properties={},
                                                description='Additional items selected',
                                            ),
                                        ),
                                    },
                                    required=[
                                        'id', 'registrationDate', 'email', 'firstName', 'lastName',
                                        'gender', 'dateOfBirth', 'tShirtSize', 'country', 'city',
                                        'phoneNumber', 'emergencyContactName', 'emergencyContactPhone'
                                    ],
                                ),
                            ),
                        },
                        required=['pagination', 'items_count', 'items'],
                    ),
                ),
                401: openapi.Response(
                    description='Unauthorized',
                    schema=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'detail': openapi.Schema(
                                type=openapi.TYPE_STRING, description='Authentication credentials were not provided.'
                            )
                        },
                        required=['detail'],
                    ),
                ),
                500: openapi.Response(
                    description='Server error',
                    schema=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'detail': openapi.Schema(
                                type=openapi.TYPE_STRING,
                                description='An unexpected error occurred on the server.',
                            )
                        },
                        required=['detail'],
                    ),
                ),
            },
        }


        post = {
            'tags': ['User Distance Registration'],
            'operation_description': 'User Distance Registration',
            'request_body': openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'email': openapi.Schema(type=openapi.TYPE_STRING, description='User email'),
                    'firstName': openapi.Schema(type=openapi.TYPE_STRING, description='User first name'),
                    'lastName': openapi.Schema(type=openapi.TYPE_STRING, description='User last name'),
                    'firstNameEng': openapi.Schema(
                        type=openapi.TYPE_STRING, description='User first name in English', nullable=True
                    ),
                    'lastNameEng': openapi.Schema(
                        type=openapi.TYPE_STRING, description='User last name in English', nullable=True
                    ),
                    'gender': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        enum=['M', 'F'],
                        description='Gender: M for Male, F for Female',
                        nullable=True,
                    ),
                    'dateOfBirth': openapi.Schema(
                        type=openapi.FORMAT_DATE,
                        description='Date of birth',
                        nullable=True,
                        default='2024-12-12'
                    ),
                    'tShirtSize': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        enum=['XXS', 'XS', 'S', 'M', 'L', 'XL', 'XXL', 'XXXL'],
                        description='T-shirt size',
                        nullable=True,
                    ),
                    'country': openapi.Schema(type=openapi.TYPE_STRING, description='Country', nullable=True),
                    'city': openapi.Schema(type=openapi.TYPE_STRING, description='City', nullable=True),
                    'phoneNumber': openapi.Schema(type=openapi.TYPE_STRING, description='Phone number', nullable=True),
                    'sportsClub': openapi.Schema(type=openapi.TYPE_STRING, description='Sports club', nullable=True),
                    'emergencyContactName': openapi.Schema(
                        type=openapi.TYPE_STRING, description='Emergency contact name', nullable=True
                    ),
                    'emergencyContactPhone': openapi.Schema(
                        type=openapi.TYPE_STRING, description='Emergency contact phone number', nullable=True
                    ),
                    'promoCode': openapi.Schema(
                        type=openapi.TYPE_INTEGER, description='Promo code ID', nullable=True
                    ),
                    'additionalItems': openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Items(type=openapi.TYPE_INTEGER),
                        description='List of additional item IDs',
                        nullable=True,
                    ),
                },
                required=['firstName', 'lastName'],
            ),
            'responses': {
                201: openapi.Response('Registration Successful', UserDistanceRegistrationSerializer),
                400: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING, description='Invalid data or already registred for this distance.'
                        )
                    },
                    required=['detail'],
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
                404: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING, description='Distance not found or related items are invalid.'
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
        }

        
    class UserRegistrationsViewSwagger:
        get = {
            'tags': ['User Distance Registration'],
            'operation_description': (
                'Get all registrations of the authenticated user. Use "status" query parameter to filter:\n'
                '- "active" for active registrations\n'
                '- "archive" for archived registrations'
            ),
            'manual_parameters': [
                openapi.Parameter(
                    'status',
                    openapi.IN_QUERY,
                    description='Filter by status: "active" or "archive".',
                    type=openapi.TYPE_STRING,
                    enum=['active', 'archive'],
                ),
                openapi.Parameter(
                    'page', openapi.IN_QUERY, description='Page number for pagination', type=openapi.TYPE_STRING
                ),
            ],
            'responses': {
                200: openapi.Response(
                    description='List of user registrations',
                    schema=openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='Registration ID'),
                                'registrationDate': openapi.Schema(
                                    type=openapi.FORMAT_DATETIME, description='Date of registration'
                                ),
                                'distance': openapi.Schema(
                                    type=openapi.TYPE_OBJECT,
                                    properties={
                                        'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='Distance ID'),
                                        'name': openapi.Schema(type=openapi.TYPE_STRING, description='Distance name'),
                                    },
                                    required=['id', 'name'],
                                ),
                                'firstName': openapi.Schema(type=openapi.TYPE_STRING, description='First name'),
                                'lastName': openapi.Schema(type=openapi.TYPE_STRING, description='Last name'),
                                'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email'),
                                'promoCode': openapi.Schema(
                                    type=openapi.TYPE_STRING, description='Applied promo code', nullable=True
                                ),
                                'additionalItems': openapi.Schema(
                                    type=openapi.TYPE_ARRAY,
                                    items=openapi.Schema(
                                        type=openapi.TYPE_OBJECT,
                                        properties={
                                            'id': openapi.Schema(
                                                type=openapi.TYPE_INTEGER, description='Additional item ID'
                                            ),
                                        },
                                        required=['id'],
                                    ),
                                    description='List of additional items selected',
                                    nullable=True,
                                ),
                            },
                            required=['id', 'registrationDate', 'distance', 'firstName', 'lastName', 'email'],
                        ),
                    ),
                ),
                401: openapi.Response(
                    description='Unauthorized',
                    schema=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'detail': openapi.Schema(
                                type=openapi.TYPE_STRING, description='Authentication credentials were not provided.'
                            )
                        },
                        required=['detail'],
                    ),
                ),
                500: openapi.Response(
                    description='Server error',
                    schema=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'detail': openapi.Schema(
                                type=openapi.TYPE_STRING,
                                description='An unexpected error occurred on the server.',
                            )
                        },
                        required=['detail'],
                    ),
                ),
            },
        }


    class AdditionalProfileList:
        get = {
            'tags': ['Additional Profile'],
            'operation_description': 'Get a list of additional profiles',
            'responses': {
                200: AdditionalProfileSerializer(many=True),
                400: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Invalid request parameters or data.',
                        )
                    },
                    required=['detail'],
                ),
                401: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING, description='Invalid credentials.'
                        )
                    },
                    required=['detail'],
                ),
                403: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Insufficient permissions to access this resource.',
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
        }

        post = {
            'tags': ['Additional Profile'],
            'operation_description': 'Create an additional profile',
            'request_body': AdditionalProfileSerializer,
            'responses': {
                201: AdditionalProfileSerializer,
                400: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Invalid request parameters or data.',
                        )
                    },
                    required=['detail'],
                ),
                401: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING, description='Invalid credentials.'
                        )
                    },
                    required=['detail'],
                ),
                403: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Insufficient permissions to create this resource.',
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
        }

    class AdditionalProfileDetail:
        get = {
            'tags': ['Additional Profile'],
            'operation_description': 'Get an additional profile',
            'responses': {
                200: AdditionalProfileSerializer,
                400: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Invalid request parameters or data.',
                        )
                    },
                    required=['detail'],
                ),
                401: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING, description='Invalid credentials.'
                        )
                    },
                    required=['detail'],
                ),
                403: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Insufficient permissions to access this resource.',
                        )
                    },
                    required=['detail'],
                ),
                404: openapi.Response(description='Profile not found'),
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
        }

        patch = {
            'tags': ['Additional Profile'],
            'operation_description': 'Partially update an additional profile',
            'request_body': AdditionalProfileSerializer,
            'responses': {
                200: AdditionalProfileSerializer,
                400: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Invalid request parameters or data.',
                        )
                    },
                    required=['detail'],
                ),
                401: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING, description='Invalid credentials.'
                        )
                    },
                    required=['detail'],
                ),
                403: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Insufficient permissions to update this resource.',
                        )
                    },
                    required=['detail'],
                ),
                404: openapi.Response(description='Profile not found'),
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
        }

        put = {
            'tags': ['Additional Profile'],
            'operation_description': 'Update an additional profile',
            'request_body': AdditionalProfileSerializer,
            'responses': {
                200: AdditionalProfileSerializer,
                400: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Invalid request parameters or data.',
                        )
                    },
                    required=['detail'],
                ),
                401: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING, description='Invalid credentials.'
                        )
                    },
                    required=['detail'],
                ),
                403: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Insufficient permissions to update this resource.',
                        )
                    },
                    required=['detail'],
                ),
                404: openapi.Response(description='Profile not found'),
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
        }

        delete = {
            'tags': ['Additional Profile'],
            'operation_description': 'Delete an additional profile',
            'responses': {
                204: openapi.Response(description='Profile deleted successfully'),
                400: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Invalid request parameters or data.',
                        )
                    },
                    required=['detail'],
                ),
                401: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING, description='Invalid credentials.'
                        )
                    },
                    required=['detail'],
                ),
                403: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Insufficient permissions to delete this resource.',
                        )
                    },
                    required=['detail'],
                ),
                404: openapi.Response(description='Profile not found'),
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
        }


    class Profile:
        get = {
            'tags': ['Profile'],
            'responses': {
                200: UserProfileSerializer,
                400: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Invalid request parameters or data.',
                        )
                    },
                    required=['detail'],
                ),
                401: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING, description='Invalid credentials.'
                        )
                    },
                    required=['detail'],
                ),
                403: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Insufficient permissions to access this resource.',
                        )
                    },
                    required=['detail'],
                ),
                404: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='The requested resource does not exist.',
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
            'operation_description': 'Get user profile data',
        }

        put = {
            'tags': ['Profile'],
            'request_body': UserProfileSerializer,
            'responses': {
                200: UserProfileSerializer,
                400: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Invalid request parameters or data.',
                        )
                    },
                    required=['detail'],
                ),
                401: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING, description='Invalid credentials.'
                        )
                    },
                    required=['detail'],
                ),
                403: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Insufficient permissions to update this resource.',
                        )
                    },
                    required=['detail'],
                ),
                404: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='The resource to update does not exist.',
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
            'operation_description': 'Update user profile data',
        }

        patch = {
            'tags': ['Profile'],
            'request_body': UserProfileSerializer,
            'responses': {
                200: UserProfileSerializer,
                400: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Invalid request parameters or data.',
                        )
                    },
                    required=['detail'],
                ),
                401: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING, description='Invalid credentials.'
                        )
                    },
                    required=['detail'],
                ),
                403: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Insufficient permissions to partially update this resource.',
                        )
                    },
                    required=['detail'],
                ),
                404: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='The resource to partially update does not exist.',
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
            'operation_description': 'Partial update of user profile data',
        }


    class LikeEventView:
        post = {
            'tags': ['Event Like'],
            'operation_description': 'Like an event by its ID',
            'responses': {
                200: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING, description='Event liked successfully.'
                        )
                    },
                    required=['detail'],
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

        delete = {
            'tags': ['Event Like'],
            'operation_description': 'Unlike an event by its ID',
            'responses': {
                200: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'message': openapi.Schema(
                            type=openapi.TYPE_STRING, description='Event unliked successfully.'
                        )
                    },
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

    class LikedEventsView:
        get = {
            'tags': ['Event Like'],
            'operation_description': 'Retrieve a list of liked events with pagination',
            'manual_parameters': [
                openapi.Parameter(
                    'status',
                    openapi.IN_QUERY,
                    description='Filter by status: "active" or "archive".',
                    type=openapi.TYPE_STRING,
                    enum=['active', 'archive'],
                ),
                openapi.Parameter(
                    'page',
                    openapi.IN_QUERY,
                    description='Page number for pagination',
                    type=openapi.TYPE_STRING
                ),
            ],
            'responses': {
                200: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'pagination': openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'next_page': openapi.Schema(
                                    type=openapi.TYPE_STRING,
                                    nullable=True,
                                    description='URL of the next page, or null if there are no more pages'
                                ),
                                'current_page': openapi.Schema(
                                    type=openapi.TYPE_INTEGER,
                                    description='Current page number'
                                ),
                                'previous_page': openapi.Schema(
                                    type=openapi.TYPE_STRING,
                                    nullable=True,
                                    description='URL of the previous page, or null if on the first page'
                                ),
                                'num_pages': openapi.Schema(
                                    type=openapi.TYPE_INTEGER,
                                    description='Total number of pages'
                                ),
                            },
                            required=['current_page', 'num_pages']
                        ),
                        'items_count': openapi.Schema(
                            type=openapi.TYPE_INTEGER,
                            description='Total number of items'
                        ),
                        'items': openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Schema(
                                type=openapi.TYPE_OBJECT,
                                properties={
                                    'id': openapi.Schema(
                                        type=openapi.TYPE_INTEGER,
                                        description='Event ID'
                                    ),
                                    'name': openapi.Schema(
                                        type=openapi.TYPE_STRING,
                                        description='Event Name'
                                    ),
                                    'dateFrom': openapi.Schema(
                                        type=openapi.TYPE_STRING,
                                        format='date',
                                        description='Start date of the event'
                                    ),
                                    'dateTo': openapi.Schema(
                                        type=openapi.TYPE_STRING,
                                        format='date',
                                        description='End date of the event'
                                    ),
                                },
                                required=['id', 'name', 'dateFrom', 'dateTo']
                            ),
                            description='List of events'
                        ),
                    },
                    required=['pagination', 'items_count', 'items'],
                    description='Paginated list of liked events.',
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
