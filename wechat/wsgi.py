"""
WSGI config for wechat project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.local")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.local")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

    import django.core.handlers.wsgi
    import sys

    application = django.core.handlers.wsgi.WSGIHandler()
