from drf_yasg import openapi

from event.serializers import CompetitionTypeSerializer


class SwaggerDocs:
    class CompetitionsTypeViewSet:
        get = {
            'tags': ['Competition Type'],
            'operation_description': 'Get an Competition Type',
            'responses': {
                200: CompetitionTypeSerializer,
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
                            type=openapi.TYPE_STRING, description='No CompetitionType matches the given query.'
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
            'tags': ['Competition Type'],
            'request_body': CompetitionTypeSerializer,
            'responses': {
                201: CompetitionTypeSerializer,
                400: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING, description='competition type with this name already exists.'
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
                            type=openapi.TYPE_STRING, description='No CompetitionType matches the given query.'
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
                            type=openapi.TYPE_STRING, description='No CompetitionType matches the given query.'
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
            'operation_description': 'Update Competition Type',
        }

        patch = {
            'tags': ['Competition Type'],
            'request_body': CompetitionTypeSerializer,
            'responses': {
                201: CompetitionTypeSerializer,
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
                            type=openapi.TYPE_STRING, description='No CompetitionType matches the given query.'
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
            'operation_description': 'Partial update Competition Type',
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
                            type=openapi.TYPE_STRING, description='No CompetitionType matches the given query.'
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
                            description='Error message indicating why the request was invalid.'
                        )
                    },
                    required=['detail'],
                ),
                403: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Error message indicating insufficient permissions.'
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
