from .base import *


DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'postgres',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
    },
}

STATIC_ROOT = '/var/www/static/'
MEDIA_ROOT = '/var/www/media/'
STATIC_BUNDLE_URL = '/static/bundle.js'
