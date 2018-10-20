from enum import Enum
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
import uuid


class HousingAd(models.Model):
    class COUNTRIES(Enum):
        senegal = ('SN', 'Sénégal')
        cameroun = ('CM', 'Caméroun')
        ivory_coast = ('CI', "Côte d'Ivoire")
        nigeria = ('NG', 'Nigéria')
        ghana = ('GH', 'Ghana')
        maroc = ('MA', 'Maroc')
        kenya = ('KE', 'Kenya')
        tunisia = ('TN', 'Tunisie')

        @classmethod
        def get_value(cls, member):
            return cls[member].value[0]

    uuid = models.UUIDField(db_index=True, default=uuid.uuid4(), editable=False)
    published = models.DateTimeField(auto_now_add=True, blank=True)
    title = models.CharField(max_length=250, default='Nouvelle annonce')
    description = models.TextField(blank=True)
    source = models.CharField(max_length=250)
    link = models.CharField(max_length=250)
    image = models.CharField(max_length=250, blank=True)
    country = models.CharField(choices=[x.value for x in COUNTRIES], default='SN', max_length=2)
    location = models.CharField(max_length=250, blank=True)
    surface_area = models.IntegerField(blank=True, null=True)
    price = models.BigIntegerField(blank=True, null=True)
    rooms = models.IntegerField(blank=True, null=True)
    ad_type = models.CharField(choices=[('Housing', 'Logement')], default='Housing', max_length=20, blank=True)
    housing_type = models.CharField(choices=[('House', 'Maison'), ('Flat', 'Appartement')],
                                    default='Flat', max_length=20, blank=True)
    transaction_type = models.CharField(choices=[('buy', 'Vente'), ('rent', 'Location')],
                                        default='rent', max_length=20, blank=True)

    class Meta:
        ordering = ('published',)

    def __str__(self):
        return self.title


class LandAd(models.Model):
    class COUNTRIES(Enum):
        senegal = ('SN', 'Sénégal')
        cameroun = ('CM', 'Caméroun')
        ivory_coast = ('CI', "Côte d'Ivoire")
        nigeria = ('NG', 'Nigéria')
        ghana = ('GH', 'Ghana')
        maroc = ('MA', 'Maroc')
        kenya = ('KE', 'Kenya')
        tunisia = ('TN', 'Tunisie')

        @classmethod
        def get_value(cls, member):
            return cls[member].value[0]

    uuid = models.UUIDField(db_index=True, default=uuid.uuid4(), editable=False)
    published = models.DateTimeField(auto_now_add=True, blank=True)
    title = models.CharField(max_length=250, default='Nouvelle annonce')
    description = models.TextField(blank=True)
    source = models.CharField(max_length=250)
    link = models.CharField(max_length=250)
    image = models.CharField(max_length=250, blank=True)
    country = models.CharField(choices=[x.value for x in COUNTRIES], default='SN', max_length=2)
    location = models.CharField(max_length=250, blank=True)
    surface_area = models.IntegerField(blank=True, null=True)
    price = models.BigIntegerField(blank=True, null=True)
    status = models.CharField(choices=[('Approved', 'Titré'), ('Not Approved', 'Non Titré')],
                              default='Approved', max_length=20, blank=True)
    ad_type = models.CharField(choices=[('land', 'Terrain')], default='Land', max_length=20)
    transaction_type = models.CharField(choices=[('buy', 'Vente'), ('rent', 'Location')],
                                        default='rent', max_length=20, blank=True)

    class Meta:
        ordering = ('published',)

    def __str__(self):
        return self.title


class JobAd(models.Model):
    class COUNTRIES(Enum):
        senegal = ('SN', 'Sénégal')
        cameroun = ('CM', 'Caméroun')
        ivory_coast = ('CI', "Côte d'Ivoire")
        nigeria = ('NG', 'Nigéria')
        ghana = ('GH', 'Ghana')
        maroc = ('MA', 'Maroc')
        kenya = ('KE', 'Kenya')
        tunisia = ('TN', 'Tunisie')

        @classmethod
        def get_value(cls, member):
            return cls[member].value[0]

    uuid = models.UUIDField(db_index=True, default=uuid.uuid4(), editable=False)
    published = models.DateTimeField(auto_now_add=True, blank=True)
    title = models.CharField(max_length=250, default='Nouvelle annonce')
    description = models.TextField(blank=True)
    source = models.CharField(max_length=250)
    link = models.CharField(max_length=250)
    image = models.CharField(max_length=250, blank=True)
    country = models.CharField(choices=[x.value for x in COUNTRIES], default='SN', max_length=2)
    location = models.CharField(max_length=250, blank=True)
    ad_type = models.CharField(choices=[('Job', 'Emploi')], default='Job', max_length=20, blank=True)
    subjects = models.CharField(max_length=250, blank=True)
    gross_salary = models.BigIntegerField(blank=True, null=True)
    contract_type = models.CharField(choices=[('CDI', 'CDI'), ('CDD', 'CDD'), ('Undefined', 'Non précisé')],
                                     default='Undefined', max_length=20, blank=True)

    class Meta:
        ordering = ('published',)

    def __str__(self):
        return self.title