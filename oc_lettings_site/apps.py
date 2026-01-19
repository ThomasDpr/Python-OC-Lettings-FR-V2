"""
Application configuration module for the oc_lettings_site application.

This module contains the Django AppConfig class that configures
the oc_lettings_site application.
"""

from django.apps import AppConfig


class OCLettingsSiteConfig(AppConfig):
    """
    Django application configuration for oc_lettings_site.

    This class configures the main application settings including
    the application name used by Django's app registry.
    """

    name = 'oc_lettings_site'
