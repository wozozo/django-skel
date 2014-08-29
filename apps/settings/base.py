"""
Django settings for {{ project_name }} project.

For more information on this file, see
https://docs.djangoproject.com/en/{{ docs_version }}/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/

global_settings.py, see
https://github.com/django/django/blob/master/django/conf/global_settings.py
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
DJANGO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SITE_NAME = os.path.basename(BASE_DIR)

####################
# CORE             #
####################

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/{{ docs_version }}/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '{{ secret_key }}'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.humanize',

    'storages',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'apps.urls'

WSGI_APPLICATION = 'apps.wsgi.application'


# Database
# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/{{ docs_version }}/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

APPEND_SLASH = False

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.normpath(os.path.join(BASE_DIR, 'media'))

# URL that handles the media served from MEDIA_ROOT.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.normpath(os.path.join(BASE_DIR, 'static'))

# URL that handles the static files served from STATIC_ROOT.
# Static files (CSS, JavaScript, Images)
# Example: "http://example.com/static/", "http://static.example.com/"
# https://docs.djangoproject.com/en/{{ docs_version }}/howto/static-files/
STATIC_URL = '/static/'

# List of locations of the template source files, in search order.
TEMPLATE_DIRS = (
    os.path.normpath(os.path.join(BASE_DIR, 'templates')),
)

###############
# STATICFILES #
###############

# A list of locations of additional static files
STATICFILES_DIRS = (
    os.path.normpath(os.path.join(BASE_DIR, 'assets')),
)

###########
# STORAGE #
###########

# See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html#settings
STATICFILES_STORAGE = DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', '')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME', '')
AWS_AUTO_CREATE_BUCKET = True
AWS_QUERYSTRING_AUTH = False

# AWS cache settings, don't change unless you know what you're doing:
AWS_EXPIREY = 60 * 60 * 24 * 7
AWS_HEADERS = {
    'Cache-Control': 'max-age=%d, s-maxage=%d, must-revalidate' % (
        AWS_EXPIREY, AWS_EXPIREY)
}

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = 'https://s3.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME

EKUBO_DOMAIN = os.environ.get('EKUBO_DOMAIN', '')
