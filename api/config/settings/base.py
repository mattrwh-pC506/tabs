# -*- coding: utf-8 -*-
"""
Django settings for ACM project.
For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
import os
import datetime
import json
import environ

from os.path import join, abspath, dirname

here = lambda *dirs: join(abspath(dirname(__file__)), *dirs)
BASE_DIR = here('..', '..')
root = lambda *dirs: join(abspath(BASE_DIR), *dirs)
ROOT = lambda base: join(dirname(__file__)+"/../../", base)

secrets = {}
try:
    # grab environment variables from a shared JSON file
    with open(ROOT('config/secrets.json')) as f:
        secrets = json.loads(f.read())
except IOError:
    # fall back to environment variables (for Heroku)
    secrets = {
        'db-engine': os.environ.get('db_engine', ""),
        'dev-db-name': os.environ.get('dev_db_name', ""),
        'dev-db-host': os.environ.get('dev_db_host', ""),
        'dev-db-user': os.environ.get('dev_db_user', ""),
        'dev-db-password': os.environ.get('dev_db_password', ""),
        'dev-db-port': os.environ.get('dev_db_port', ""),
        'secret-key': os.environ.get('secret_key', "")
    }

env = environ.Env()

# APP CONFIGURATION
# -----------------------------------------------------------------------------
DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Admin
    'django.contrib.admin',
    'django.contrib.admindocs',
)

THIRD_PARTY_APPS = (
    'rest_framework',
)

LOCAL_APPS = (
    "api",
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIDDLEWARE CONFIGURATION
# -----------------------------------------------------------------------------
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# DEBUG
# -----------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

# EMAIL CONFIGURATION
# -----------------------------------------------------------------------------
EMAIL_HOST = ''  # Need to set if using email
EMAIL_HOST_PASSWORD = 'password'  # Need to set if using email
EMAIL_HOST_USER = ''  # Need to set if using email
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# MANAGER CONFIGURATION
# -----------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    # List admin contact here as a 2-tuple i.e. ('admin name', 'admin email'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

# DATABASE CONFIGURATION
# -----------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
    }
}

# GENERAL CONFIGURATION
# -----------------------------------------------------------------------------
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Denver'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

# Output Etag header. Not sure it's needed...
# See: https://docs.djangoproject.com/en/1.8/ref/settings/#use-etags
USE_ETAGS = True

# International Translation - not necessary so turned off for performance
# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = False

# Localize Data
# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# Use timezones
# See: https://docs.djangoproject.com/en/1.8/ref/settings/#use-tz
USE_TZ = True

# TEMPLATE CONFIGURATION
# -----------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        'DIRS': [
            ROOT('api/templates/'),
        ],
        'OPTIONS': {
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
            'debug': DEBUG,
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

MEDIA_ROOT = root('media')

STATIC_ROOT = root('collected_static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    root('assets'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Security depends on this being secret
SECRET_KEY = 'secret'  # redefined in settings_private

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
)

# URL Configuration
# -----------------------------------------------------------------------------
ROOT_URLCONF = 'config.urls'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'config.wsgi.application'

APPEND_SLASH = True

# Third-Party Settings
# -----------------------------------------------------------------------------
REST_FRAMEWORK = {
    # Use hyperlinked styles by default.
    # Only used if the `serializer_class` attribute is not set on a view.
    'DEFAULT_MODEL_SERIALIZER_CLASS': (
        'rest_framework.serializers.HyperlinkedModelSerializer',
    ),

    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    )
}

JWT_AUTH = {
    # give authentication 30 days to expire
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=30)
}
