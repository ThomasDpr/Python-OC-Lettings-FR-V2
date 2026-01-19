"""
Application configuration module for the lettings application.

This module contains the Django AppConfig class that configures
the lettings application.
"""

from django.apps import AppConfig


class LettingsConfig(AppConfig):
    """
    Django application configuration for the lettings app.

    This class configures the lettings application settings
    including the application name used by Django's app registry.
    """

    name = 'lettings'
