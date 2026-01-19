"""
URL configuration module for the lettings application.

This module defines the URL patterns for the lettings app,
including the lettings list view and individual letting detail views.
"""

from django.urls import path
from . import views

app_name = "lettings"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:letting_id>/", views.letting, name="letting"),
]
