"""
Views module for the lettings application.

This module contains view functions for displaying the list of lettings
and individual letting details.
"""

from django.shortcuts import render, get_object_or_404

from .models import Letting
import logging
logger = logging.getLogger(__name__)


def index(request):
    """
    Display the list of all available lettings.

    Retrieves all Letting objects from the database and renders them
    in the lettings index template.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered template with the list of lettings.
    """
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """
    Display the details of a specific letting.

    Retrieves a single Letting object by its ID and renders its details.
    Returns a 404 error if the letting is not found.

    Args:
        request: The HTTP request object.
        letting_id: The unique identifier of the letting to display.

    Returns:
        HttpResponse: The rendered template with the letting details.

    Raises:
        Http404: If no letting matches the given ID.
    """
    try:
        letting = get_object_or_404(Letting, id=letting_id)
    except Exception:
        logger.error(
            "Letting not found",
            extra={"letting_id": letting_id}
        )
        raise

    return render(request, "lettings/letting.html", {"letting": letting})
