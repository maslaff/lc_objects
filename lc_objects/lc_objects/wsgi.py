"""
WSGI config for lc_objects project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""
from dotenv import load_dotenv
import os
import sys

project_folder = os.path.expanduser('~/www/lc_objects')
load_dotenv(os.path.join(project_folder, '.env'))

if project_folder not in sys.path:
    sys.path.append(project_folder)

os.environ['DJANGO_SETTINGS_MODULE'] = 'lc_objects.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
