"""Development settings for {{ project_name }}."""

import os

from base import *

####################
# CORE             #
####################

DEBUG = True

TEMPLATE_DEBUG = DEBUG

# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.normpath(os.path.join(DJANGO_DIR, 'default.db')),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

INSTALLED_APPS += (
    'debug_toolbar',
    'django_extensions',
)

#########
# CACHE #
#########

# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

##############
# MIDDLEWARE #
##############

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
