from django.urls import path, include
from rest_framework.routers import DefaultRouter
from landcrowdy.users import views

router = DefaultRouter()
router.register('', views.UserViewSet)

urlpatterns = [
    path('users/', include(router.urls)),
]