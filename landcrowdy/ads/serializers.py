from rest_framework import serializers
from landcrowdy.ads.models import HousingAd, LandAd, JobAd, AD_TYPE_CHOICES, COUNTRY_CHOICES

class HousingAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = HousingAd
        fields = ('id', 'title', 'description', 'source', 'link', 'image', 'country', 'location', 'ad_type',
                  'surface_area', 'price', 'rooms', 'housing_type', 'transaction_type')


class LandAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandAd
        fields = ('id', 'title', 'description', 'source', 'link', 'image', 'country', 'location', 'ad_type',
                  'surface_area', 'price', 'status', 'transaction_type')


class JobAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobAd
        fields = ('id', 'title', 'description', 'source', 'link', 'image', 'country', 'location', 'ad_type',
                  'subjects', 'gross_salary', 'contract_type')