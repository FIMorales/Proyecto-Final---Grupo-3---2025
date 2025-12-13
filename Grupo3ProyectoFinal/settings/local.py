from.base import *
import os
from pathlib import Path

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # SOLUCIÓN: Usar BASE_DIR para apuntar al archivo db.sqlite3
        'NAME': BASE_DIR / 'db.sqlite3', 
    }
}
