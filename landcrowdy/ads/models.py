from django.db import models
from django.utils.text import slugify
from django.urls import reverse
import uuid

COUNTRY_CHOICES = sorted([('SN', 'Sénégal'), ('CM', 'Caméroun'), ('CI', "Côte d'Ivoire"), ('NG', 'Nigéria'),
                          ('GH', 'Ghana'), ('MA', 'Maroc'), ('KE', 'Kenya'), ('TN', 'Tunisie')])
AD_TYPE_CHOICES = sorted([('Housing','Logement'), ('Land', 'Terrain'), ('Job','Emploi')])

class Annonce(models.Model):
    uuid = models.UUIDField(db_index=True, default=uuid.uuid4(), editable=False, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=250, default='Nouvelle annonce')
    description = models.TextField(blank=True)
    source = models.CharField(max_length=250)
    link = models.CharField(max_length=250)
    image = models.CharField(max_length=250, blank=True)
    country = models.CharField(choices=COUNTRY_CHOICES, default='SN', max_length=2)
    location = models.CharField(max_length=250, blank=True)

    class Meta:
        ordering = ('created',)


class HousingAd(Annonce):
    surface_area = models.IntegerField(blank=True)
    price = models.IntegerField(blank=True)
    rooms = models.IntegerField(blank=True)
    ad_type = models.CharField(choices=[('Housing', 'Logement')], default='Housing', max_length=20)
    housing_type = models.CharField(choices=[('House', 'Maison'), ('Flat', 'Appartement')],
                                    default='Flat', max_length=20)
    transaction_type = models.CharField(choices=[('buy', 'Vente'), ('rent', 'Location')],
                                        default='rent', max_length=20)


class LandAd(Annonce):
    surface_area = models.IntegerField(blank=True)
    price = models.IntegerField(blank=True)
    status = models.CharField(choices=[('Approved', 'Titré'), ('Not Approved', 'Non Titré')], default='Approved', max_length=20)
    ad_type = models.CharField(choices=[('land', 'Terrain')], default='Land', max_length=20)
    transaction_type = models.CharField(choices=[('buy', 'Vente'), ('rent', 'Location')],
                                        default='rent', max_length=20)


class JobAd(Annonce):
    ad_type = models.CharField(choices=[('Job', 'Emploi')], default='Job', max_length=20)
    subjects = models.CharField(max_length=250, blank=True)
    gross_salary = models.IntegerField(blank=True)
    contract_type = models.CharField(choices=[('CDI', 'CDI'), ('CDD', 'CDD'), ('Undefined', 'Non précisé')],
                                     default='Undefined', max_length=20)
