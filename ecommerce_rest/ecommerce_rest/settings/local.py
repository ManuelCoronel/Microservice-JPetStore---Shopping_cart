
from .base import *
import os
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
MEDIA_URL = '/archivos/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'