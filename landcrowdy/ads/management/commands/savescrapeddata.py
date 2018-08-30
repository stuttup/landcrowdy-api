from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from landcrowdy.ads.models import HousingAd, LandAd, JobAd
from datetime import datetime
import json
import re
from os.path import join





class Command(BaseCommand):
    help = 'Saves scraped data to database'

    # def add_arguments(self, parser):
    # parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):

        def force_to_int(s):
            """Extracts all digits from a string and returns it as int

            :param s: String
            :return: Int
            """
            try:
                result = int(re.sub(r'\D', '', s))
            except Exception as e:
                result = 0
                print(e)
            return result

        # Remove old records
        HousingAd.objects.all().delete()
        LandAd.objects.all().delete()
        JobAd.objects.all().delete()

        # Insert new records
        self.stdout.write(self.style.SUCCESS("Inserting new records"))
        with open(join(settings.BASE_DIR, 'landcrowdy/ads/maisons.json')) as f:
            maisons = json.load(f)
        with open(join(settings.BASE_DIR, 'landcrowdy/ads/terrains.json')) as f:
            terrains = json.load(f)
        with open(join(settings.BASE_DIR, 'landcrowdy/ads/jobs.json')) as f:
            jobs = json.load(f)

        for maison in maisons:
            m = HousingAd(title=maison.get('titre', 'Test'), description=maison.get('description', ''),
                          source='https://delas.jumia.sn', ad_type='House',
                          image=maison.get('image', ''), link=maison.get('lien', ''), country='SN',
                          location=maison.get('lieu', ''),
                          surface_area=force_to_int(maison.get('superficie', '0')),
                          price=force_to_int(maison.get('prix', '0')),
                          rooms=force_to_int(maison.get('chambres', '1')),
                          housing_type=maison.get('type', 'House'),
                          published=datetime.strptime(maison.get('date', "7-8-2018 11:30").replace('.', '-'),
                                                 '%d-%m-%Y %H:%M'))
            try:
                m.save()
            except Exception as e:
                print(e)

        for terrain in terrains:
            t = LandAd(title=terrain.get('titre', 'Annonce'), description=terrain.get('description', ''),
                       image=terrain.get('image', ''), country='SN', source='https://delas.jumia.sn', ad_type='Land',
                       location=terrain.get('lieu', ''),
                       surface_area=force_to_int(terrain.get('superficie', '0')),
                       price=force_to_int(terrain.get('prix', '0')), transaction_type=terrain.get('type', 'buy'),
                       status=terrain.get('statut'),
                       published=datetime.strptime(terrain.get('date', "7-8-2018 11:30").replace('.', '-'),
                                              '%d-%m-%Y %H:%M'),
                       link=terrain.get('lien', ''), )
            try:
                t.save()
            except Exception as e:
                print(e)

        for job in jobs:
            j = JobAd(title=job.get('titre', 'Annonce'), description=job.get('description', ''),
                      image=job.get('image', ''), link=job.get('lien', ''), country='SN',
                      location=job.get('lieu', ''), subjects=job.get('domaines', ''),
                      gross_salary=job.get('salaire', 0), contract_type=job.get('type', 'CDI'),
                      published=datetime.strptime(job.get('date', "7-8-2018 11:30").replace('.', '-'),
                                             '%d-%m-%Y %H:%M'))
            try:
                j.save()
            except Exception as e:
                print(e)

        self.stdout.write(self.style.SUCCESS('Successfully saved data to database'))
