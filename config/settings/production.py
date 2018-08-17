from config.settings.base import *
from config.settings.base import env

DEBUG = env.bool('DJANGO-DEBUG', default=False)