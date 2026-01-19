#!/usr/bin/env python
"""
Django's command-line utility for administrative tasks.

This module serves as the entry point for Django management commands
such as runserver, migrate, makemigrations, and other administrative tasks.
"""

import os
import sys


def main():
    """
    Run administrative tasks for the Django project.

    Sets the default Django settings module and executes command-line
    arguments as Django management commands.

    Raises:
        ImportError: If Django is not installed or not available in PYTHONPATH.
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
