from django.urls import path, include
from rest_framework.routers import DefaultRouter
from landcrowdy.ads import views

router = DefaultRouter()
router.register('housing', views.HousingAdViewSet)
router.register('land', views.LandAdViewSet)
router.register('job', views.JobAdViewSet)

urlpatterns = [
    path('', include(router.urls)),
]