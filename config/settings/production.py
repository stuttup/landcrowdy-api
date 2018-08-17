from config.settings.base import *
from config.settings.base import env

DEBUG = False

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['localhost','127.0.0.1', '.niangular.com'])