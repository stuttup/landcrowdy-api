from landcrowdy.ads.models import LandAd, HousingAd, JobAd
from landcrowdy.ads.api.serializers import HousingAdSerializer, LandAdSerializer, JobAdSerializer
from rest_framework import permissions, viewsets
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope, IsAuthenticatedOrTokenHasScope


# Create your views here.
class HousingAdViewSet(viewsets.ModelViewSet):
    queryset = HousingAd.objects.all()
    serializer_class = HousingAdSerializer
    permission_classes = (IsAuthenticatedOrTokenHasScope, )
    lookup_field = 'uuid'
    required_scopes = ['write']


class LandAdViewSet(viewsets.ModelViewSet):
    queryset = LandAd.objects.all()
    serializer_class = LandAdSerializer
    permission_classes = (IsAuthenticatedOrTokenHasScope,)
    lookup_field = 'uuid'
    required_scopes = ['write']


class JobAdViewSet(viewsets.ModelViewSet):
    queryset = JobAd.objects.all()
    serializer_class = JobAdSerializer
    permission_classes = (IsAuthenticatedOrTokenHasScope,)
    lookup_field = 'uuid'
    required_scopes = ['write']
