"""
Admin configuration module for the lettings application.

This module registers the Address and Letting models with the Django
admin site, enabling CRUD operations through the admin interface.
"""

from django.contrib import admin
from .models import Address, Letting

admin.site.register(Address)
admin.site.register(Letting)
