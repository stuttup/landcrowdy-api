from rest_framework import serializers
from landcrowdy.ads.models import HousingAd, LandAd, JobAd


class HousingAdSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HousingAd
        fields = ('uuid', 'url', 'title', 'description', 'source', 'link', 'image', 'country', 'location', 'ad_type',
                  'surface_area', 'price', 'rooms', 'housing_type', 'transaction_type')
        extra_kwargs = {
            'url': {'lookup_field': 'uuid'}
        }


class LandAdSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LandAd
        fields = ('uuid', 'url', 'title', 'description', 'source', 'link', 'image', 'country', 'location', 'ad_type',
                  'surface_area', 'price', 'status', 'transaction_type')
        extra_kwargs = {
            'url': {'lookup_field': 'uuid'}
        }


class JobAdSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JobAd
        fields = ('uuid', 'url', 'title', 'description', 'source', 'link', 'image', 'country', 'location', 'ad_type',
                  'subjects', 'gross_salary', 'contract_type')
        extra_kwargs = {
            'url': {'lookup_field': 'uuid'}
        }
