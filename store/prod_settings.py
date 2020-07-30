import os

import dj_database_url

from .settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
#debug_option = os.environ.get('DEBUG').lower()
# if debug_option == 'true':
DEBUG = False
# else:
#    DEBUG = False

#ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(';')
ALLOWED_HOSTS = ['still-plateau-17088.herokuapp.com']
#ALLOWED_HOSTS = ['morning-depths-38898.herokuapp.com']
# Database
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL')
    )
}

# Mail Server
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_HOST = 'smtp.sendgrid.net'
#EMAIL_HOST_USER = 'apikey'
#EMAIL_HOST_PASSWORD = os.getenv('SENDGRID_API_KEY')
#EMAIL_PORT = 587
#EMAIL_USE_TLS = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL ')
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'  # this is exactly the value 'apikey'
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
EMAIL_PORT = 587
EMAIL_USE_TLS = True
