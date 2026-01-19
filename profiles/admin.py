"""
Admin configuration module for the profiles application.

This module registers the Profile model with the Django admin site,
enabling CRUD operations through the admin interface.
"""

from django.contrib import admin
from .models import Profile

admin.site.register(Profile)
