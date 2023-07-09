from .environment_setting import env, os, BASE_DIR
import django_heroku
from .application_setting import (
    DJANGO_APPLICATIONS,
    CUSTOM_APPLICATIONS,
    THIRD_PARTY_APPLICATIONS,
)


SECRET_KEY = env("SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = ["*"]


ROOT_URLCONF = 'coresite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

INSTALLED_APPS = [
    *DJANGO_APPLICATIONS,
    *CUSTOM_APPLICATIONS,
    *THIRD_PARTY_APPLICATIONS,
]


WSGI_APPLICATION = 'coresite.wsgi.application'


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
django_heroku.settings(locals())
