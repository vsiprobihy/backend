from functools import wraps

from django.core.exceptions import PermissionDenied

from event.distance_details.models import DistanceEvent
from event.models import Event
from organization.models import Organization, Organizer
from utils.custom_exceptions import BadRequestError, NotFoundError


def check_organization_access_decorator(event_extractor):
    """
    A decorator to check if the user has access to the organization associated with the event.

    :param event_extractor: A function that extracts the Event instance from the request and parameters.
    :raises PermissionDenied: If the user does not have access to the organization.
    :raises Http404: If the extracted Event does not exist.
    """

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(self, request, *args, **kwargs):
            try:
                event = event_extractor(request, *args, **kwargs)  # noqa: F841
            except Event.DoesNotExist:

                raise NotFoundError('Event not found.')

            user = request.user
            organization_id = kwargs.get('organization_id')

            organizer_access_exists = Organizer.objects.filter(user=user, organization_id=organization_id).exists()

            if not organizer_access_exists:
                raise PermissionDenied('You do not have permission to access this event.')

            return view_func(self, request, *args, **kwargs)

        return _wrapped_view

    return decorator


def check_organizer_access_decorator(organizer_extractor):
    """
    A decorator to check if the user has access to the organization associated with the event.

    :param organizer_extractor: A function that extracts the Event instance from the request and parameters.
    :raises PermissionDenied: If the user does not have access to the organization.
    :raises Http404: If the extracted Event does not exist.
    """

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(self, request, *args, **kwargs):
            if request.data:
                if request.data.get('organization_id') != kwargs.get('organization_id'):
                    raise BadRequestError('Parameter organization_id dont match with organization id')

            try:
                organizer = organizer_extractor(request, *args, **kwargs)  # noqa: F841

            except Organizer.DoesNotExist:
                raise NotFoundError('Organization not found.')

            user = request.user
            organization_id = kwargs.get('organization_id')

            organizer_access_exists = Organizer.objects.filter(user=user, organization_id=organization_id).exists()

            if not organizer_access_exists:
                raise PermissionDenied('You do not have permission to access this organization.')

            return view_func(self, request, *args, **kwargs)

        return _wrapped_view

    return decorator


def extract_organization_directly(request, *args, **kwargs):
    """
    Extracts the Organization instance directly using the organization_id parameter.

    :param request: The HTTP request object.
    :raises OrganizationAccess.DoesNotExist: If the Organization with the given ID does not exist.
    :return: The Organization instance.
    """
    organization_id = kwargs.get('organization_id')
    return Organizer.objects.get(pk=organization_id)


def extract_event_directly(request, *args, **kwargs):
    """
    Extracts the Event instance directly using the event_id parameter.

    :param request: The HTTP request object.
    :raises Event.DoesNotExist: If the Event with the given ID does not exist.
    :return: The Event instance.
    """
    event_id = kwargs.get('event_id')
    return Event.objects.get(pk=event_id)


def check_distance_access_decorator():
    """
    A decorator to check if the user has access to the distance associated with the event.

    :raises PermissionDenied: If the user does not have access to the distance.
    :raises Http404: If the extracted DistanceEvent does not exist.
    """

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(self, request, *args, **kwargs):
            user = request.user
            organization_id = kwargs.get('organization_id')
            event_id = kwargs.get('event_id', None)
            distance_id = kwargs.get('distance_id', None)

            if not user or not organization_id or not event_id or not distance_id:
                raise BadRequestError('Bad request')

            organization = Organization.objects.filter(organizerOrganization__user=user, pk=organization_id).first()

            if organization is None:
                raise NotFoundError('Organization not found.')

            event = Event.objects.filter(organization_id=organization.id, pk=event_id).first()
            if event is None:
                raise NotFoundError('Event not found.')

            distance = DistanceEvent.objects.filter(event_id=event.id, pk=distance_id).first()
            if distance is None:
                raise NotFoundError('Distance not found.')

            return view_func(self, request, *args, **kwargs)

        return _wrapped_view

    return decorator
