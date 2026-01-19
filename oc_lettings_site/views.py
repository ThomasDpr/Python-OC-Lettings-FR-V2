"""
Views module for the oc_lettings_site application.

This module contains the main view functions for the homepage
and custom error handlers (404 and 500).
"""

from django.shortcuts import render


def index(request):
    """
    Display the homepage of the OC Lettings site.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered homepage template.
    """
    return render(request, "oc_lettings_site/index.html")


def custom_404(request, exception):
    """
    Handle 404 Not Found errors with a custom template.

    Args:
        request: The HTTP request object.
        exception: The exception that triggered the 404 error.

    Returns:
        HttpResponse: The rendered 404 error page with status code 404.
    """
    return render(request, "404.html", status=404)


def custom_500(request):
    """
    Handle 500 Internal Server errors with a custom template.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered 500 error page with status code 500.
    """
    return render(request, "500.html", status=500)
