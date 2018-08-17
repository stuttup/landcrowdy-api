from django.urls import path, include
from rest_framework.routers import DefaultRouter
from landcrowdy.ads.api import viewsets

router = DefaultRouter()
router.register('housing', viewsets.HousingAdViewSet)
router.register('land', viewsets.LandAdViewSet)
router.register('job', viewsets.JobAdViewSet)

urlpatterns = [
    path('', include(router.urls)),
]