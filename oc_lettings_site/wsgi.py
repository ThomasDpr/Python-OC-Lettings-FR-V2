"""
WSGI configuration module for the oc_lettings_site project.

This module exposes the WSGI callable as a module-level variable named
``application``. It is used by WSGI servers to serve the application.

For more information on this file, see:
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')

application = get_wsgi_application()
