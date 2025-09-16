"""
WSGI config for Zomato_Clone_Food_Delivery_Web_Application project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Zomato_Clone_Food_Delivery_Web_Application.settings')

application = get_wsgi_application()
