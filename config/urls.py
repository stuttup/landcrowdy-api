"""landcrowdy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view


schema_view = get_schema_view(title='Landcrowdy API')

urlpatterns = [
    path('api/v1/schema/', schema_view),
    path('api/v1/', include('landcrowdy.ads.urls')),
    path('api/v1/', include('landcrowdy.users.urls')),
    path('api/v1/admin/', admin.site.urls),
    path('api/v1/o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
