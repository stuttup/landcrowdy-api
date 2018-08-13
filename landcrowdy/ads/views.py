from django.shortcuts import render
from landcrowdy.ads.models import LandAd, HousingAd, JobAd
from landcrowdy.ads.serializers import HousingAdSerializer, LandAdSerializer, JobAdSerializer
from rest_framework import generics, permissions


# Create your views here.
class HousingAdList(generics.ListCreateAPIView):
    queryset = HousingAd.objects.all()
    serializer_class = HousingAdSerializer
    permission_classes = (permissions.IsAuthenticated,)


class HousingAdDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HousingAd.objects.all()
    serializer_class = HousingAdSerializer
    permission_classes = (permissions.IsAuthenticated,)


class LandAdList(generics.ListCreateAPIView):
    queryset = LandAd.objects.all()
    serializer_class = LandAdSerializer
    permission_classes = (permissions.IsAuthenticated,)

class LandAdDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LandAd.objects.all()
    serializer_class = LandAdSerializer
    permission_classes = (permissions.IsAuthenticated,)


class JobAdList(generics.ListCreateAPIView):
    queryset = JobAd.objects.all()
    serializer_class = JobAdSerializer
    permission_classes = (permissions.IsAuthenticated,)


class JobAdDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobAd.objects.all()
    serializer_class = JobAdSerializer
    permission_classes = (permissions.IsAuthenticated)