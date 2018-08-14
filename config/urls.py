"""landcrowdy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('api/v1/', include('landcrowdy.ads.urls')),
    path('api/v1/users/', include('landcrowdy.users.urls')),
    path('api/v1/admin/', admin.site.urls),
    path('api/v1/auth/', include('rest_framework.urls')),
]
