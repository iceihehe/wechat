#!/usr/bin/env python
import os
import sys


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.local")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.local")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

    import django.core.handlers.wsgi

    application = django.core.handlers.wsgi.WSGIHandler()
