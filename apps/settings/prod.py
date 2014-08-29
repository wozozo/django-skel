"""Production settings for {{ project_name }}."""

from base import *

####################
# CORE             #
####################

# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'localhost'

EMAIL_HOST_PASSWORD = ''

EMAIL_HOST_USER = ''

EMAIL_PORT = 25

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
EMAIL_USE_TLS = False

# See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = 'root@localhost'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '{{ project_name }}',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

#########
# CACHE #
#########

# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': '',
    }
}
