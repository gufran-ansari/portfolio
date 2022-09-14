"""
Django settings for codezyners project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
import django_on_heroku
from pathlib import Path
from django.contrib import messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.environ.get('SECRET_KEY')
SECRET_KEY = "5cab4443be24fa938eb9c3d6bc796d0309d773eb514a0cdf"

# SECURITY WARNING: don't run with debug turned on in production!
# When Testing
DEBUG = True
# When Live
# DEBUG = False

ALLOWED_HOSTS = ['*', 'codezyners.herokuapp.com', 'localhost', '127.0.0.1']


# Application definition
INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Deployment
    'django_filters',
    'storages',
    'boto3',

    # App
    "portfolio",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # WhiteNoise Middleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'codezyners.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'codezyners.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# --------------------------------------------------------------------------------------------

""" CUSTOM SETTINGS """

# --------------------------------------------------------------------------------------------

""" Static Settings """
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

""" Media Setting """
MEDIA_URL = '/image/'
MEDIA_ROOT = os.path.join(BASE_DIR, "static/image")

""" WhiteNoise Setting """
WHITENOISE_AUTOREFRESH = True
# Whitenoise cache policy
WHITENOISE_MAX_AGE = 31536000 if not DEBUG else 0  # 1 year

""" AWS Configuration """
AWS_ACCESS_KEY_ID = "AKIAUBYA6OGTUVTMJ2FQ"
AWS_SECRET_ACCESS_KEY = "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"
AWS_STORAGE_BUCKET_NAME = "codezyners"

""" S3 Configuration """
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

""" If file doesn't load, add these settings """
AWS_S3_REGION_NAME = 'us-east-2'  # change to your region
AWS_S3_SIGNATURE_VERSION = 's3v4'  # this will change S3 version from V2 to V4

AWS_S3_HOST = 'us-east-2'
S3_USE_SIGV4 = True


""" Pagination Setting """
PAGINATION_SETTINGS = {
    'PAGE_RANGE_DISPLAYED': 3,
    'MARGIN_PAGES_DISPLAYED': 2,

    'SHOW_FIRST_PAGE_WHEN_INVALID': True,
}

""" Django Heroku Configuration 

pip install django_heroku 
changed to 
pip install django_on_heroku
"""
django_on_heroku.settings(locals())


""" Message Tag """
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}


""" Email Configurations """
"""
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_ID')
EMAIL_HOST_PASSWORD = os.environ.get('PASSWORD')
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


AWS_ACCESS_KEY_ID = "AKIAUBYA6OGTUVTMJ2FQ"
AWS_SECRET_ACCESS_KEY = "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"
AWS_STORAGE_BUCKET_NAME = "codezyners"
"""
