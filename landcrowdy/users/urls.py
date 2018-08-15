from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_auth.registration.views import SocialAccountListView, SocialAccountDisconnectView
from landcrowdy.users import views

router = DefaultRouter()
router.register('', views.UserViewSet)

urlpatterns = [
    path('users/', include(router.urls)),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('rest-auth/facebook/', views.FacebookLogin.as_view(), name='fb_login'),
    path('rest-auth/facebook/connect/', views.FacebookConnect.as_view(), name='fb_connect'),
    path('rest-auth/social-accounts/', SocialAccountListView.as_view(), name='social_account_list'),
    path('rest-auth/social-accounts/<int:pk>/', SocialAccountDisconnectView.as_view(), name='social_account_disconnect'),
]