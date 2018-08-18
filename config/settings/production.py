from config.settings.base import *
from config.settings.base import env

DEBUG = False

SECRET_KEY = env('SECRET_KEY', default='c#-!x^di-(n7@h@_2p@j(%^ce#8-@m=ager%x_zfqq%034qfdb')

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['localhost','127.0.0.1', '.niangular.com'])
# Database
#DATABASES = {}
#DATABASES['default'] = env.db('DATABASE_URL')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': '127.0.0.1',
        'PORT': '5432',
	'ATOMIC_REQUESTS': True,
	'CONN_MAX_AGE': env.int('CONN_MAX_AGE', default=60)
    }
}
