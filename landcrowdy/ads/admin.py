from django.contrib import admin
from landcrowdy.ads.models import HousingAd, LandAd, JobAd


@admin.register(HousingAd)
class HousingAdModelAdmin(admin.ModelAdmin):
    list_display = ('ad_type', 'title', )


@admin.register(LandAd)
class LandAdModelAdmin(admin.ModelAdmin):
    list_display = ('ad_type', 'title', )

@admin.register(JobAd)
class JobAdModelAdmin(admin.ModelAdmin):
    list_display = ('ad_type', 'title', )