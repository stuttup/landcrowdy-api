from config.settings.base import *
from config.settings.base import env

DEBUG = False

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['localhost','127.0.0.1', '.niangular.com'])
# Database
DATABASES['default'] = env.db('DATABASE_URL')
DATABASES['default']['ATOMIC_REQUESTS'] = True
DATABASES['default']['CONN_MAX_AGE'] = env.int('CONN_MAX_AGE', default=60)