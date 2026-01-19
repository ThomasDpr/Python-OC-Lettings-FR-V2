"""
URL configuration module for the profiles application.

This module defines the URL patterns for the profiles app,
including the profiles list view and individual profile detail views.
"""

from django.urls import path
from . import views

app_name = "profiles"

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:username>/", views.profile, name="profile"),
]
