from drf_yasg import openapi


class Responce:
    EventResponse = openapi.Response(
            'Event created successfully',
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                required=[
                    'id', 'name', 'competition_type', 'date_from', 'date_to',
                    'place', 'place_region', 'organizer', 'distances'
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
                    'competition_type': openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            required=['name'],
                            properties={
                                'name': openapi.Schema(
                                    type=openapi.TYPE_STRING,
                                    description='Type of competition'
                                ),
                            },
                        ),
                    ),
                    'date_from': openapi.Schema(
                        type=openapi.FORMAT_DATE,
                        description='Event start date'
                    ),
                    'date_to': openapi.Schema(
                        type=openapi.FORMAT_DATE,
                        description='Event end date'
                    ),
                    'place': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description='Event location'
                    ),
                    'place_region': openapi.Schema(
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
                    'registration_link': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description='Registration link for the event'
                    ),
                    'hide_participants': openapi.Schema(
                        type=openapi.TYPE_BOOLEAN,
                        description='Hide participants flag'
                    ),
                    'schedule_pdf': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        nullable=True,
                        description='Schedule PDF link'
                    ),
                    'organizer': openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        required=['id', 'users', 'name', 'email'],
                        properties={
                            'id': openapi.Schema(
                                type=openapi.TYPE_INTEGER,
                                description='Organizer ID'
                            ),
                            'users': openapi.Schema(
                                type=openapi.TYPE_ARRAY,
                                items=openapi.Schema(
                                    type=openapi.TYPE_OBJECT,
                                    required=['user', 'role'],
                                    properties={
                                        'user': openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description='User email'
                                        ),
                                        'role': openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description='User role'
                                        ),
                                    },
                                ),
                            ),
                            'name': openapi.Schema(
                                type=openapi.TYPE_STRING,
                                description='Organizer name'
                            ),
                            'site_url': openapi.Schema(
                                type=openapi.TYPE_STRING,
                                description='Organizer website'
                            ),
                            'phone_number': openapi.Schema(
                                type=openapi.TYPE_STRING,
                                description='Organizer phone number'
                            ),
                            'email': openapi.Schema(
                                type=openapi.TYPE_STRING,
                                description='Organizer email'
                            ),
                            'instagram_url': openapi.Schema(
                                type=openapi.TYPE_STRING,
                                description='Organizer Instagram URL'
                            ),
                            'facebook_url': openapi.Schema(
                                type=openapi.TYPE_STRING,
                                description='Organizer Facebook URL'
                            ),
                            'telegram_url': openapi.Schema(
                                type=openapi.TYPE_STRING,
                                description='Organizer Telegram URL'
                            ),
                        },
                    ),
                    'distances': openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            required=[
                                'id', 'name', 'competition_type', 'category',
                                'start_number_from', 'start_number_to',
                                'allow_registration', 'length',
                                'promo_only_registration', 'cost', 'is_free',
                                'show_name_on_number', 'show_start_number', 'event'
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
                                'competition_type': openapi.Schema(
                                    type=openapi.TYPE_STRING,
                                    description='Type of competition'
                                ),
                                'category': openapi.Schema(
                                    type=openapi.TYPE_STRING,
                                    description='Category of participants'
                                ),
                                'allow_registration': openapi.Schema(
                                    type=openapi.TYPE_BOOLEAN,
                                    description='Flag for registration availability'
                                ),
                                'length': openapi.Schema(
                                    type=openapi.TYPE_STRING,
                                    description='Distance length'
                                ),
                                'start_number_from': openapi.Schema(
                                    type=openapi.TYPE_INTEGER,
                                    description='Start number range (from)'
                                ),
                                'start_number_to': openapi.Schema(
                                    type=openapi.TYPE_INTEGER,
                                    description='Start number range (to)'
                                ),
                                'age_from': openapi.Schema(
                                    type=openapi.TYPE_INTEGER,
                                    description='Minimum age'
                                ),
                                'age_to': openapi.Schema(
                                    type=openapi.TYPE_INTEGER,
                                    description='Maximum age'
                                ),
                                'cost': openapi.Schema(
                                    type=openapi.TYPE_STRING,
                                    description='Cost of participation'
                                ),
                                'is_free': openapi.Schema(
                                    type=openapi.TYPE_BOOLEAN,
                                    description='Flag indicating free participation'
                                ),
                                'promo_only_registration': openapi.Schema(
                                    type=openapi.TYPE_BOOLEAN,
                                    description='Promo-only registration flag'
                                ),
                                'show_name_on_number': openapi.Schema(
                                    type=openapi.TYPE_BOOLEAN,
                                    description='Flag to show name on number'
                                ),
                                'show_start_number': openapi.Schema(
                                    type=openapi.TYPE_BOOLEAN,
                                    description='Flag to show start number'
                                ),
                                'event': openapi.Schema(
                                    type=openapi.TYPE_INTEGER,
                                    description='Associated event ID'
                                ),
                                'additional_options': openapi.Schema(
                                    type=openapi.TYPE_ARRAY,
                                    items=openapi.Schema(
                                        type=openapi.TYPE_OBJECT,
                                        required=['id', 'item_type', 'price', 'distance'],
                                        properties={
                                            'id': openapi.Schema(
                                                type=openapi.TYPE_INTEGER,
                                                description='Option ID'
                                            ),
                                            'item_type': openapi.Schema(
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
                            },
                        ),
                    ),
                    'extended_description': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description='Detailed description of the event'
                    ),
                },
            ),
        )


class Request:

    EventRequestBody = openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'name': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Name of the event',
                            default='Winter Wonderland Run 2024',
                        ),
                        'competition_type': openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Schema(
                                type=openapi.TYPE_OBJECT,
                                properties={
                                    'name': openapi.Schema(
                                        type=openapi.TYPE_STRING,
                                        description='Type of competition',
                                        default='running',
                                    )
                                },
                                required=['name']
                            ),
                            description='List of competition types',
                        ),
                        'date_from': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            format=openapi.FORMAT_DATE,
                            description='Event start date',
                            default='2024-10-28',
                        ),
                        'date_to': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            format=openapi.FORMAT_DATE,
                            description='Event end date',
                            default='2024-10-28',
                        ),
                        'place': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Location of the event',
                            default='Lviv',
                        ),
                        'place_region': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Location of the event',
                            default='lviv_region',
                        ),
                        'description': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Event description',
                            default='Embrace the winter spirit with our Winter Wonderland Run!',
                        ),
                        'registration_link': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            format=openapi.FORMAT_URI,
                            description='Registration link',
                            default='http://site.com/registration/winter-wonderland-run-2024',
                        ),
                        'hide_participants': openapi.Schema(
                            type=openapi.TYPE_BOOLEAN,
                            description='Whether to hide participants',
                            default=True,
                        ),
                        'organization_id': openapi.Schema(
                            type=openapi.TYPE_INTEGER,
                            description='ID of the organizer',
                            default=1,
                        ),
                        'distances': openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Schema(
                                type=openapi.TYPE_OBJECT,
                                properties={
                                    'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='id',
                                                            default=1),
                                    'name': openapi.Schema(type=openapi.TYPE_STRING, description='Name of the distance',
                                                        default='5km Snow Run'),
                                    'competition_type': openapi.Schema(type=openapi.TYPE_STRING,
                                                                    description='Type of competition',
                                                                    default='running'),
                                    'category': openapi.Schema(type=openapi.TYPE_STRING,
                                                            description='Category of participants', default='adults'),

                                    'length': openapi.Schema(type=openapi.TYPE_NUMBER,
                                                            description='Length of the distance in km', default=5.0),

                                    'start_number_from': openapi.Schema(type=openapi.TYPE_INTEGER,
                                                                        description='Starting number', default=1),

                                    'start_number_to': openapi.Schema(type=openapi.TYPE_INTEGER,
                                                                    description='Ending number', default=300),

                                    'show_start_number': openapi.Schema(type=openapi.TYPE_BOOLEAN,
                                                                        description='Show start number', default=True),

                                    'show_name_on_number': openapi.Schema(type=openapi.TYPE_BOOLEAN,
                                                                        description='Show name on the number',
                                                                        default=True),
                                    'age_from': openapi.Schema(type=openapi.TYPE_INTEGER, description='Minimum age',
                                                            default=16),
                                    'age_to': openapi.Schema(type=openapi.TYPE_INTEGER, description='Maximum age',
                                                            default=60),
                                    'cost': openapi.Schema(type=openapi.TYPE_NUMBER, description='Cost of the distance',
                                                        default=55),
                                    'is_free': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Is the distance free',  # noqa: E501
                                                            default=False),
                                    'promo_only_registration': openapi.Schema(type=openapi.TYPE_BOOLEAN,
                                                                            description='Promo-only registration',
                                                                            default=False),
                                    'allow_registration': openapi.Schema(type=openapi.TYPE_BOOLEAN,
                                                                        description='Allow registration', default=True),

                                    'additional_options': openapi.Schema(
                                        type=openapi.TYPE_ARRAY,
                                        items=openapi.Schema(
                                            type=openapi.TYPE_OBJECT,
                                            properties={
                                                'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='id',
                                                                        default=1),
                                                'item_type': openapi.Schema(type=openapi.TYPE_STRING,
                                                                            description='Type of additional option',
                                                                            default='t_shirt'),
                                                'price': openapi.Schema(type=openapi.TYPE_NUMBER,
                                                                        description='Price of additional option',
                                                                        default=250),
                                            },
                                            required=['item_type', 'price'],
                                        ),
                                        description='Additional options for the distance'
                                    ),
                                },
                                required=[
                                    'name', 'competition_type', 'category',
                                    'start_number_from', 'start_number_to',
                                    'allow_registration', 'length',
                                    'promo_only_registration', 'cost', 'is_free',
                                    'show_name_on_number', 'show_start_number', 'event'
                                ],
                            ),
                            description='List of distances',
                        ),
                        'extended_description': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Extended description of the event',
                            default='Experience the beauty of winter while getting fit!',
                        ),
                    },
                    required=[
                        'name',
                        'competition_type',
                        'date_from',
                        'date_to',
                        'place',
                        'place_region',
                        'organization_id',
                        'additional_items',
                        'distances',
                    ],
                )


    EventRequestBodyPost = openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'name': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Name of the event',
                            default='Winter Wonderland Run 2024',
                        ),
                        'competition_type': openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Schema(
                                type=openapi.TYPE_OBJECT,
                                properties={
                                    'name': openapi.Schema(
                                        type=openapi.TYPE_STRING,
                                        description='Type of competition',
                                        default='running',
                                    )
                                },
                                required=['name']
                            ),
                            description='List of competition types',
                        ),
                        'date_from': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            format=openapi.FORMAT_DATE,
                            description='Event start date',
                            default='2024-10-28',
                        ),
                        'date_to': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            format=openapi.FORMAT_DATE,
                            description='Event end date',
                            default='2024-10-28',
                        ),
                        'place': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Location of the event',
                            default='Lviv',
                        ),
                        'place_region': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Location of the event',
                            default='lviv_region',
                        ),
                        'description': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Event description',
                            default='Embrace the winter spirit with our Winter Wonderland Run!',
                        ),
                        'registration_link': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            format=openapi.FORMAT_URI,
                            description='Registration link',
                            default='http://site.com/registration/winter-wonderland-run-2024',
                        ),
                        'hide_participants': openapi.Schema(
                            type=openapi.TYPE_BOOLEAN,
                            description='Whether to hide participants',
                            default=True,
                        ),
                        'organization_id': openapi.Schema(
                            type=openapi.TYPE_INTEGER,
                            description='ID of the organizer',
                            default=1,
                        ),
                        'distances': openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Schema(
                                type=openapi.TYPE_OBJECT,
                                properties={
                                    'name': openapi.Schema(type=openapi.TYPE_STRING, description='Name of the distance',
                                                        default='5km Snow Run'),
                                    'competition_type': openapi.Schema(type=openapi.TYPE_STRING,
                                                                    description='Type of competition',
                                                                    default='running'),
                                    'category': openapi.Schema(type=openapi.TYPE_STRING,
                                                            description='Category of participants', default='adults'),

                                    'length': openapi.Schema(type=openapi.TYPE_NUMBER,
                                                            description='Length of the distance in km', default=5.0),

                                    'start_number_from': openapi.Schema(type=openapi.TYPE_INTEGER,
                                                                        description='Starting number', default=1),

                                    'start_number_to': openapi.Schema(type=openapi.TYPE_INTEGER,
                                                                    description='Ending number', default=300),

                                    'show_start_number': openapi.Schema(type=openapi.TYPE_BOOLEAN,
                                                                        description='Show start number', default=True),

                                    'show_name_on_number': openapi.Schema(type=openapi.TYPE_BOOLEAN,
                                                                        description='Show name on the number',
                                                                        default=True),
                                    'age_from': openapi.Schema(type=openapi.TYPE_INTEGER, description='Minimum age',
                                                            default=16),
                                    'age_to': openapi.Schema(type=openapi.TYPE_INTEGER, description='Maximum age',
                                                            default=60),
                                    'cost': openapi.Schema(type=openapi.TYPE_NUMBER, description='Cost of the distance',
                                                        default=55),
                                    'is_free': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Is the distance free',  # noqa: E501
                                                            default=False),
                                    'promo_only_registration': openapi.Schema(type=openapi.TYPE_BOOLEAN,
                                                                            description='Promo-only registration',
                                                                            default=False),
                                    'allow_registration': openapi.Schema(type=openapi.TYPE_BOOLEAN,
                                                                        description='Allow registration', default=True),

                                    'additional_options': openapi.Schema(
                                        type=openapi.TYPE_ARRAY,
                                        items=openapi.Schema(
                                            type=openapi.TYPE_OBJECT,
                                            properties={
                                                'item_type': openapi.Schema(type=openapi.TYPE_STRING,
                                                                            description='Type of additional option',
                                                                            default='t_shirt'),
                                                'price': openapi.Schema(type=openapi.TYPE_NUMBER,
                                                                        description='Price of additional option',
                                                                        default=250),
                                            },
                                            required=['item_type', 'price'],
                                        ),
                                        description='Additional options for the distance'
                                    ),
                                },
                                required=[
                                    'name', 'competition_type', 'category',
                                    'start_number_from', 'start_number_to',
                                    'allow_registration', 'length',
                                    'promo_only_registration', 'cost', 'is_free',
                                    'show_name_on_number', 'show_start_number', 'event'
                                ],
                            ),
                            description='List of distances',
                        ),
                        'extended_description': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Extended description of the event',
                            default='Experience the beauty of winter while getting fit!',
                        ),
                    },
                    required=[
                        'name',
                        'competition_type',
                        'date_from',
                        'date_to',
                        'place',
                        'place_region',
                        'organization_id',
                        'additional_items',
                        'distances',
                    ],
                )