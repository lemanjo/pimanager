"""
Django settings for pimanager project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
import os

# Function for correct server timezone
from lib.timezone import gettz

# Import secret key or gen one if needed.
try:
    from secret_key import *
except ImportError:
    SETTINGS_DIR=os.path.abspath(os.path.dirname(__file__))
    generate_secret_key(os.path.join(SETTINGS_DIR, 'secret_key.py'))
    from secret_key import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

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
    'pamauth',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'pimanager.lib.middleware.RequireLoginMiddleware',
)

ROOT_URLCONF = 'pimanager.urls'

WSGI_APPLICATION = 'pimanager.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = gettz()

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

# Template dirs
TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__),'templates'),
)


# Login variables
LOGIN_URL = '/login'

# Login needed (default all sites)
LOGIN_REQUIRED_URLS = (
    r'/(.*)$',
)
LOGIN_REQUIRED_URLS_EXCEPTIONS = (
    r'/login(.*)$',
    r'/logout(.*)$',
)