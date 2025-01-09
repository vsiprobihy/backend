from drf_yasg import openapi

from event.serializers import UpdateEventStatusSerializer  # noqa
from swagger.event_variables import Request, Responce


class SwaggerDocs:

    class EventsListCreateView:
        get = {
            'tags': ['Event'],
            'operation_description': 'Retrieve event list with pagination and details.',
            'manual_parameters': [
                openapi.Parameter(
                    'archives',
                    openapi.IN_QUERY,
                    description=(
                        'Indicates whether to include archived records. '
                        'Use "archives=true" to filter by archived data.'
                    ),
                    type=openapi.TYPE_STRING,
                    example='true',
                ),
            ],
            'responses': {
                200: openapi.Response(
                    'Event list retrieved successfully',
                    schema=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        required=[
                            'pagination', 'items_count', 'items'
                        ],
                        properties={
                            'pagination': openapi.Schema(
                                type=openapi.TYPE_OBJECT,
                                required=['current_page', 'num_pages'],
                                properties={
                                    'next_page': openapi.Schema(
                                        type=openapi.TYPE_INTEGER,
                                        nullable=True,
                                        description='Next page number in pagination'
                                    ),
                                    'current_page': openapi.Schema(
                                        type=openapi.TYPE_INTEGER,
                                        description='Current page number'
                                    ),
                                    'previous_page': openapi.Schema(
                                        type=openapi.TYPE_INTEGER,
                                        nullable=True,
                                        description='Previous page number in pagination'
                                    ),
                                    'num_pages': openapi.Schema(
                                        type=openapi.TYPE_INTEGER,
                                        description='Total number of pages'
                                    ),
                                },
                            ),
                            'items_count': openapi.Schema(
                                type=openapi.TYPE_INTEGER,
                                description='Total number of items'
                            ),
                            'items': openapi.Schema(
                                type=openapi.TYPE_ARRAY,
                                items=openapi.Schema(
                                    type=openapi.TYPE_OBJECT,
                                    required=[
                                        'id', 'name', 'competitionType', 'dateFrom', 'dateTo', 'place',
                                        'placeRegion', 'organizer', 'distances'
                                    ],
                                    properties={
                                        'id': openapi.Schema(
                                            type=openapi.TYPE_INTEGER,
                                            description='Event ID'
                                        ),
                                        'name': openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description='Event name'
                                        ),
                                        'competitionType': openapi.Schema(
                                            type=openapi.TYPE_ARRAY,
                                            items=openapi.Schema(
                                                type=openapi.TYPE_OBJECT,
                                                required=['id', 'name'],
                                                properties={
                                                    'id': openapi.Schema(
                                                        type=openapi.TYPE_INTEGER,
                                                        description='Competition type ID'
                                                    ),
                                                    'name': openapi.Schema(
                                                        type=openapi.TYPE_STRING,
                                                        description='Competition type name'
                                                    ),
                                                },
                                            ),
                                        ),
                                        'dateFrom': openapi.Schema(
                                            type=openapi.FORMAT_DATE,
                                            description='Event start date'
                                        ),
                                        'dateTo': openapi.Schema(
                                            type=openapi.FORMAT_DATE,
                                            description='Event end date'
                                        ),
                                        'place': openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description='Event location'
                                        ),
                                        'placeRegion': openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description='Region of the event'
                                        ),
                                        'photos': openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            nullable=True,
                                            description='Event photos URL'
                                        ),
                                        'description': openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description='Short description of the event'
                                        ),
                                        'registrationLink': openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description='Registration link for the event'
                                        ),
                                        'hideParticipants': openapi.Schema(
                                            type=openapi.TYPE_BOOLEAN,
                                            description='Flag to hide participants'
                                        ),
                                        'schedulePdf': openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            nullable=True,
                                            description='Schedule PDF link'
                                        ),
                                        'coOrganizer': openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description='Co-Organizer of the event'
                                        ),
                                        'organizer': openapi.Schema(
                                            type=openapi.TYPE_OBJECT,
                                            required=['id', 'user', 'organization'],
                                            properties={
                                                'id': openapi.Schema(
                                                    type=openapi.TYPE_INTEGER,
                                                    description='Organizer ID'
                                                ),
                                                'user': openapi.Schema(
                                                    type=openapi.TYPE_STRING,
                                                    description='Organizer user email'
                                                ),
                                                'organization': openapi.Schema(
                                                    type=openapi.TYPE_STRING,
                                                    description='Organizer organization name'
                                                ),
                                            },
                                        ),
                                        'distances': openapi.Schema(
                                            type=openapi.TYPE_ARRAY,
                                            items=openapi.Schema(
                                                type=openapi.TYPE_OBJECT,
                                                required=[
                                                    'id', 'name', 'competitionType', 'category', 'allowRegistration',
                                                    'length', 'startNumberFrom', 'startNumberTo', 'cost', 'isFree',
                                                    'promoOnlyRegistration', 'showNameOnNumber',
                                                    'showStartNumber', 'event'
                                                ],
                                                properties={
                                                    'id': openapi.Schema(
                                                        type=openapi.TYPE_INTEGER,
                                                        description='Distance ID'
                                                    ),
                                                    'name': openapi.Schema(
                                                        type=openapi.TYPE_STRING,
                                                        description='Distance name'
                                                    ),
                                                    'competitionType': openapi.Schema(
                                                        type=openapi.TYPE_STRING,
                                                        description='Competition type for this distance'
                                                    ),
                                                    'category': openapi.Schema(
                                                        type=openapi.TYPE_STRING,
                                                        description='Category of participants'
                                                    ),
                                                    'allowRegistration': openapi.Schema(
                                                        type=openapi.TYPE_BOOLEAN,
                                                        description='Flag for registration availability'
                                                    ),
                                                    'length': openapi.Schema(
                                                        type=openapi.TYPE_STRING,
                                                        description='Distance length'
                                                    ),
                                                    'startNumberFrom': openapi.Schema(
                                                        type=openapi.TYPE_INTEGER,
                                                        description='Start number range (from)'
                                                    ),
                                                    'startNumberTo': openapi.Schema(
                                                        type=openapi.TYPE_INTEGER,
                                                        description='Start number range (to)'
                                                    ),
                                                    'ageFrom': openapi.Schema(
                                                        type=openapi.TYPE_INTEGER,
                                                        description='Minimum age for the distance'
                                                    ),
                                                    'ageTo': openapi.Schema(
                                                        type=openapi.TYPE_INTEGER,
                                                        description='Maximum age for the distance'
                                                    ),
                                                    'cost': openapi.Schema(
                                                        type=openapi.TYPE_STRING,
                                                        description='Cost for participation'
                                                    ),
                                                    'isFree': openapi.Schema(
                                                        type=openapi.TYPE_BOOLEAN,
                                                        description='Whether the participation is free'
                                                    ),
                                                    'promoOnlyRegistration': openapi.Schema(
                                                        type=openapi.TYPE_BOOLEAN,
                                                        description='Promo-only registration flag'
                                                    ),
                                                    'showNameOnNumber': openapi.Schema(
                                                        type=openapi.TYPE_BOOLEAN,
                                                        description='Whether to show name on number'
                                                    ),
                                                    'showStartNumber': openapi.Schema(
                                                        type=openapi.TYPE_BOOLEAN,
                                                        description='Whether to show start number'
                                                    ),
                                                    'event': openapi.Schema(
                                                        type=openapi.TYPE_INTEGER,
                                                        description='Associated event ID'
                                                    ),
                                                    'additionalOptions': openapi.Schema(
                                                        type=openapi.TYPE_ARRAY,
                                                        items=openapi.Schema(
                                                            type=openapi.TYPE_OBJECT,
                                                            required=['id', 'itemType', 'price', 'distance'],
                                                            properties={
                                                                'id': openapi.Schema(
                                                                    type=openapi.TYPE_INTEGER,
                                                                    description='Option ID'
                                                                ),
                                                                'itemType': openapi.Schema(
                                                                    type=openapi.TYPE_STRING,
                                                                    description='Type of additional item'
                                                                ),
                                                                'price': openapi.Schema(
                                                                    type=openapi.TYPE_STRING,
                                                                    description='Price of additional item'
                                                                ),
                                                                'distance': openapi.Schema(
                                                                    type=openapi.TYPE_INTEGER,
                                                                    description='Associated distance ID'
                                                                ),
                                                            },
                                                        ),
                                                    ),
                                                    'costChangeRules': openapi.Schema(
                                                        type=openapi.TYPE_ARRAY,
                                                        items=openapi.Schema(
                                                            type=openapi.TYPE_OBJECT,
                                                            required=['id', 'cost', 'fromDate'],
                                                            properties={
                                                                'id': openapi.Schema(
                                                                    type=openapi.TYPE_INTEGER,
                                                                    description='Cost change rule ID'
                                                                ),
                                                                'cost': openapi.Schema(
                                                                    type=openapi.TYPE_STRING,
                                                                    description='Updated cost for the distance'
                                                                ),
                                                                'fromParticipants': openapi.Schema(
                                                                    type=openapi.TYPE_INTEGER,
                                                                    nullable=True,
                                                                    description=(
                                                                        'Minimum number of participants to apply '
                                                                        'this rule'
                                                                    )
                                                                ),
                                                                'fromDate': openapi.Schema(
                                                                    type=openapi.TYPE_STRING,
                                                                    format=openapi.FORMAT_DATE,
                                                                    description='Date from which the cost rule applies'
                                                                ),
                                                            },
                                                        ),
                                                        description='List of cost change rules for the distance'
                                                    ),
                                                    'ageCategories': openapi.Schema(
                                                        type=openapi.TYPE_ARRAY,
                                                        items=openapi.Schema(
                                                            type=openapi.TYPE_OBJECT,
                                                            required=['id', 'name', 'gender', 'ageFrom', 'ageTo'],
                                                            properties={
                                                                'id': openapi.Schema(
                                                                    type=openapi.TYPE_INTEGER,
                                                                    description='Age category ID'
                                                                ),
                                                                'name': openapi.Schema(
                                                                    type=openapi.TYPE_STRING,
                                                                    description='Name of the age category'
                                                                ),
                                                                'gender': openapi.Schema(
                                                                    type=openapi.TYPE_STRING,
                                                                    description='Gender for the category'
                                                                ),
                                                                'ageFrom': openapi.Schema(
                                                                    type=openapi.TYPE_INTEGER,
                                                                    description='Minimum age for the category'
                                                                ),
                                                                'ageTo': openapi.Schema(
                                                                    type=openapi.TYPE_INTEGER,
                                                                    description='Maximum age for the category'
                                                                )
                                                            }
                                                        ),
                                                        description='List of age categories for the distance'
                                                    ),
                                                    'promoCodes': openapi.Schema(
                                                        type=openapi.TYPE_ARRAY,
                                                        items=openapi.Schema(
                                                            type=openapi.TYPE_OBJECT,
                                                            required=[
                                                                'id', 'name', 'promoType',
                                                                'discountValue', 'isActive'
                                                            ],
                                                            properties={
                                                                'id': openapi.Schema(
                                                                    type=openapi.TYPE_INTEGER,
                                                                    description='Promo code ID'
                                                                ),
                                                                'name': openapi.Schema(
                                                                    type=openapi.TYPE_STRING,
                                                                    description='Promo code name'
                                                                ),
                                                                'promoType': openapi.Schema(
                                                                    type=openapi.TYPE_STRING,
                                                                    description='Promo type (e.g., percentage discount)'
                                                                ),
                                                                'discountValue': openapi.Schema(
                                                                    type=openapi.TYPE_NUMBER,
                                                                    description='Discount value for the promo code'
                                                                ),
                                                                'isActive': openapi.Schema(
                                                                    type=openapi.TYPE_BOOLEAN,
                                                                    description='Whether the promo code is active'
                                                                ),
                                                                'isSingleUse': openapi.Schema(
                                                                    type=openapi.TYPE_BOOLEAN,
                                                                    description=(
                                                                        'Whether the promo code can be used only once'
                                                                    )
                                                                ),
                                                            },
                                                        ),
                                                        description='List of promo codes for the distance'
                                                    ),
                                                },
                                            ),
                                        ),
                                        'extendedDescription': openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description='Extended event description'
                                        ),
                                    },
                                ),
                            ),
                        },
                    ),
                ),
                404: 'Events not found',
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
