from drf_yasg import openapi

from event.serializers import CompetitionTypeSerializer


class SwaggerDocs:
    class CompetitionsTypeView:
        get = {
            'tags': ['Competition Type'],
            'operation_description': 'Get a Competition Type',
            'manual_parameters': [
                openapi.Parameter(
                    'page',
                    openapi.IN_QUERY,
                    description='Page number for pagination',
                    type=openapi.TYPE_INTEGER
                )
            ],
            'responses': {
                200: openapi.Response(
                    description='List of competition types with pagination',
                    schema=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'pagination': openapi.Schema(
                                type=openapi.TYPE_OBJECT,
                                properties={
                                    'next_page': openapi.Schema(
                                        type=openapi.TYPE_STRING,
                                        description='URL to the next page or null if there is no next page',
                                        nullable=True
                                    ),
                                    'current_page': openapi.Schema(
                                        type=openapi.TYPE_INTEGER,
                                        description='The current page number'
                                    ),
                                    'previous_page': openapi.Schema(
                                        type=openapi.TYPE_STRING,
                                        description='URL to the previous page or null if there is no previous page',
                                        nullable=True
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
                                items=openapi.Items(
                                    type=openapi.TYPE_OBJECT,
                                    properties={
                                        'id': openapi.Schema(
                                            type=openapi.TYPE_INTEGER,
                                            description='ID of the competition type'
                                        ),
                                        'name': openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description='Name of the competition type'
                                        )
                                    },
                                    required=['id', 'name']
                                )
                            )
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
                    required=['detail']
                ),
                403: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='You do not have permission to perform this action.'
                        )
                    },
                    required=['detail']
                ),
                404: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Competition type not found.'
                        )
                    },
                    required=['detail']
                ),
                500: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='An unexpected error occurred on the server.'
                        )
                    },
                    required=['detail']
                ),
            },
        }


        post = {
            'tags': ['Competition Type'],
            'request_body': CompetitionTypeSerializer,
            'responses': {
                201: CompetitionTypeSerializer,
                400: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING, description='Invalid competition type data.'
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
            'operation_description': 'Create a new Competition Type.',
        }

        put = {
            'tags': ['Competition Type'],
            'request_body': CompetitionTypeSerializer,
            'responses': {
                201: CompetitionTypeSerializer,
                400: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING, description='Invalid competition type data.'
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
                            type=openapi.TYPE_STRING, description='Competition type not found.'
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
            'operation_description': 'Create a new Competition Type.',
        }

        delete = {
            'tags': ['Competition Type'],
            'operation_description': 'Delete an additional profile',
            'responses': {
                204: openapi.Response(description=''),
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
                            type=openapi.TYPE_STRING, description='Competition type not found.'
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

    class ApproveOrganizerView:
        post = {
            'tags': ['Approve Organizer'],
            'operation_description': 'Approve Organizer',
            'responses': {
                200: 'Request approved and user is now an organizer.',
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

    class OrganizerRequestsListView:
        get = {
            'tags': ['Approve Organizer'],
            'operation_description': 'Retrieve all pending organizer requests.',
            'responses': {
                200: openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Items(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the request'),
                            'user': openapi.Schema(
                                type=openapi.TYPE_INTEGER,
                                description='ID of the user who made the request'
                                ),
                            'isApproved': openapi.Schema(
                                type=openapi.TYPE_BOOLEAN,
                                description='Approval status of the request'
                                ),
                            'createdAt': openapi.Schema(
                                type=openapi.TYPE_STRING,
                                format=openapi.FORMAT_DATETIME,
                                description='Date and time when the request was created'
                                ),
                        },
                    ),
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

    class UpdateEventStatusView:
        post = {
            'tags': ['Approve Event'],
            'request_body': openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'status': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description='New status of the event (e.g., pending, published, unpublished)',
                        enum=['pending', 'published', 'unpublished'],
                    ),
                },
                required=['status'],
            ),
            'operation_description': 'Update the status of an event by its ID.',
            'responses': {
                200: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'message': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Confirmation message that the event status was successfully updated.'
                        ),
                    },
                    required=['message'],
                ),
                400: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Error message indicating why the request was invalid.',
                            enum=[
                                'Status is not a valid choice.',
                                'The event status is already set to [status]. No changes were made.',
                            ]
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
                            type=openapi.TYPE_STRING, description='Event not found.'
                        )
                    },
                    required=['detail'],
                ),
            },
        }

    class PendingEventsView:
        get = {
            'tags': ['Approve Event'],
            'operation_description': 'Retrieve all events with status "pending".',
            'responses': {
                200: openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Items(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'id': openapi.Schema(
                                type=openapi.TYPE_INTEGER, description='ID of the event'
                            ),
                            'name': openapi.Schema(
                                type=openapi.TYPE_STRING, description='Name of the event'
                            ),
                            'organizer': openapi.Schema(
                                type=openapi.TYPE_STRING, description='Organizer of the event'
                            ),
                            'competitionType': openapi.Schema(
                                type=openapi.TYPE_ARRAY,
                                items=openapi.Items(type=openapi.TYPE_STRING),
                                description='Types of competitions associated with the event'
                            ),
                            'dateFrom': openapi.Schema(
                                type=openapi.TYPE_STRING,
                                format=openapi.FORMAT_DATE,
                                description='Start date of the event'
                            ),
                            'dateTo': openapi.Schema(
                                type=openapi.TYPE_STRING,
                                format=openapi.FORMAT_DATE,
                                description='End date of the event'
                            ),
                            'status': openapi.Schema(
                                type=openapi.TYPE_STRING, description='Status of the event'
                            ),
                        },
                        required=['id', 'name', 'organizer', 'competitionType', 'dateFrom', 'dateTo', 'status']
                    ),
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
