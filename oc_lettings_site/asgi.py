"""
ASGI configuration module for the oc_lettings_site project.

This module exposes the ASGI callable as a module-level variable named
``application``. It is used by ASGI servers to serve the application.

For more information on this file, see:
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')

application = get_asgi_application()
