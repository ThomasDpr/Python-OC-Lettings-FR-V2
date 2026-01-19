"""
Views module for the profiles application.

This module contains view functions for displaying the list of user profiles
and individual profile details.
"""

from django.shortcuts import render, get_object_or_404
import logging
from .models import Profile
logger = logging.getLogger(__name__)


def index(request):
    """
    Display the list of all user profiles.

    Retrieves all Profile objects from the database and renders them
    in the profiles index template.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered template with the list of profiles.
    """
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """
    Display the details of a specific user profile.

    Retrieves a single Profile object by the associated user's username
    and renders its details. Returns a 404 error if the profile is not found.

    Args:
        request: The HTTP request object.
        username: The username of the user whose profile to display.

    Returns:
        HttpResponse: The rendered template with the profile details.

    Raises:
        Http404: If no profile matches the given username.
    """
    try:
        profile = get_object_or_404(Profile, user__username=username)
    except Exception:
        logger.error(
            "Profile not found",
            extra={"username": username}
        )
        raise

    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
