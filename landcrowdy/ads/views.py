from landcrowdy.ads.models import LandAd, HousingAd, JobAd
from landcrowdy.ads.serializers import HousingAdSerializer, LandAdSerializer, JobAdSerializer
from rest_framework import permissions, viewsets


# Create your views here.
class HousingAdViewSet(viewsets.ModelViewSet):
    queryset = HousingAd.objects.all()
    serializer_class = HousingAdSerializer
    permission_classes = (permissions.IsAuthenticated,)


class LandAdViewSet(viewsets.ModelViewSet):
    queryset = LandAd.objects.all()
    serializer_class = LandAdSerializer
    permission_classes = (permissions.IsAuthenticated,)


class JobAdViewSet(viewsets.ModelViewSet):
    queryset = JobAd.objects.all()
    serializer_class = JobAdSerializer
    permission_classes = (permissions.IsAuthenticated,)



