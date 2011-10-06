import os
import sys
from os.path import dirname
relPath = dirname(dirname(dirname( os.path.abspath(__file__) )))
sys.path.append(os.path.abspath(relPath))

os.environ['DJANGO_SETTINGS_MODULE'] = 'streetfighters.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

