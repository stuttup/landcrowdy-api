from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from landcrowdy.ads import views

urlpatterns = [
    path('housing/', views.HousingAdList.as_view()),
    path('housing/<int:pk>', views.HousingAdDetail.as_view()),
    path('land/', views.LandAdList.as_view()),
    path('land/<int:pk>', views.LandAdDetail.as_view()),
    path('job/', views.JobAdList.as_view()),
    path('job/<int:pk>', views.JobAdDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)