from django.urls import path, include
from rest_framework.routers import DefaultRouter
from landcrowdy.users.api import viewsets

router = DefaultRouter()
router.register('users', viewsets.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]