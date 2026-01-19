"""
Application configuration module for the profiles application.

This module contains the Django AppConfig class that configures
the profiles application.
"""

from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
    Django application configuration for the profiles app.

    This class configures the profiles application settings
    including the application name used by Django's app registry.
    """

    name = 'profiles'
