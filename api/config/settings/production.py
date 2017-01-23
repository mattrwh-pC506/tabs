# -*- coding: utf-8 -*-
from .base import *

# DATABASE CONFIGURATION
# -----------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': secrets['db-engine'],
        'NAME': secrets['dev-db-name'],
        'USER': secrets['dev-db-user'],
        'PASSWORD': secrets['dev-db-password'],
        'HOST': secrets['dev-db-host'],
        'PORT': secrets['dev-db-port']
    }
}

EMAIL_HOST_PASSWORD = secrets['email-password']

SECRET_KEY = secrets['secret-key']

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# SITE CONFIGURATION
# -----------------------------------------------------------------------------
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/1.6/ref/settings/#allowed-hosts
# Allow all host headers
ALLOWED_HOSTS = ['*']
# END SITE CONFIGURATION
