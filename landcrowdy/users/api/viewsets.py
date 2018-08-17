from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope, IsAuthenticatedOrTokenHasScope

from landcrowdy.users.api.serializers import UserSerializer
from landcrowdy.users.api.permissions import IsAdminOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrTokenHasScope,)
    lookup_field = 'uuid'
    required_scopes = ['write']
