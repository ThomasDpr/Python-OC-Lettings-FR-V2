"""
URL configuration module for the oc_lettings_site project.

This module defines the root URL patterns for the entire application,
including the homepage, lettings app, profiles app, and admin site.
It also configures custom error handlers for 404 and 500 errors.
"""

from django.contrib import admin
from django.urls import path, include

from . import views

handler404 = "oc_lettings_site.views.custom_404"
handler500 = "oc_lettings_site.views.custom_500"


def trigger_error(request):
    division_by_zero = 1 / 0
    return division_by_zero


urlpatterns = [
    path("", views.index, name="index"),
    path("lettings/", include("lettings.urls")),
    path("profiles/", include("profiles.urls")),
    path("admin/", admin.site.urls),
    path("sentry-debug/", trigger_error),
]
