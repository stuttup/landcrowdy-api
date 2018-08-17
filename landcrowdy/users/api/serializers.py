from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    """
    class Meta:
        model = get_user_model()
        fields = ('uuid', 'url', 'username', 'email', 'phone', 'first_name', 'last_name')
        extra_kwargs = {
            'url': {'lookup_field': 'uuid'}
        }