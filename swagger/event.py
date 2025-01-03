from drf_yasg import openapi

from event.serializers import UpdateEventStatusSerializer  # noqa
from swagger.event_variables import Request, Responce


class SwaggerDocs:

    class EventsListCreateView:
        get = {
            'tags': ['Event'],
            'operation_description': 'Retrieve event details by ID.',
            'manual_parameters': [
                openapi.Parameter(
                    'archives',
                    openapi.IN_QUERY,
                    description='Indicates whether to include archived records. Use "archives=true" to filter by archived data.',  # noqa: E501
                    type=openapi.TYPE_STRING,
                    example='true',
                ),
            ],
            'responses': {
                200: Responce.EventResponse,
                404: 'Event not found',
            },
        }

        post = {
            'tags': ['Event'],
            'request_body': Request.EventRequestBodyPost,
            'responses': {
                201: Responce.EventResponse,
                400: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING, description='Bad request'
                        )
                    },
                    required=['detail'],
                ),
                409: openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING, description='The competition type does not exist.'
                        )
                    },
                    required=['detail'],
                ),
            },
            'operation_description': 'Create a new event with all related details including organizer, additional items, and distances.',  # noqa: E501
        }

    class EventDetailView:
        get = {
            'tags': ['Event'],
            'responses': {
                200: Responce.EventResponse,
                404: 'Event not found',
            },
            'operation_description': 'Retrieve event details by ID.',
        }

        put = {
            'tags': ['Event'],
            'request_body': Request.EventRequestBody,
            'responses': {
                200: Responce.EventResponse,
                404: 'Event not found',
            },
            'operation_description': 'Update event details without organizer, additional_items, or distances fields.',
        }

        patch = {
            'tags': ['Event'],
            'request_body': Request.EventRequestBody,
            'responses': {
                200: Responce.EventResponse,
                404: 'Event not found',
            },
            'operation_description': 'Partially update event details without organizer, additional_items, or distances fields.',  # noqa: E501
        }

        delete = {
            'tags': ['Event'],
            'responses': {
                204: 'Event deleted successfully',
                404: 'Event not found',
            },
            'operation_description': 'Delete an event by ID.',
        }
