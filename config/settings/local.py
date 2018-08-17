from config.settings.base import *
from config.settings.base import env

DEBUG = True

SECRET_KEY = env('SECRET_KEY', default='c#-!x^di-(n7@h@_2p@j(%^ce#8-@m=ager%x_zfqq%034qfdb')

ALLOWED_HOSTS = ["localhost","0.0.0.0","127.0.0.1",]
