# -*- coding: utf-8 -*-
from datetime import datetime
import json
import re
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.settings.base")

from landcrowdy.ads.models import HousingAd, LandAd, JobAd



def force_to_int(s):
    """Extracts all digits from a string and returns it as int

    :param s: String
    :return: Int
    """
    try:
        result = int(re.sub(r'\D', '', s))
    except:
        result = 0
    return result

def delete_records():
    print("Removing previous records")
    try:
        HousingAd.objects.filter(id>1).delete()
        HousingAd.objects.filter(id>1).delete()
        JobAd.objects.filter(id>1).delete()
    except:
        print("Problem deleting objects")

def insert_records():
    print("Inserting new records")
    with open('./maisons.json') as f:
        maisons = json.load(f)
    with open('./terrains.json') as f:
        terrains = json.load(f)
    with open('./jobs.json') as f:
        jobs = json.load(f)

    for maison in maisons:
        m = HousingAd(titre=maison.get('titre', 'Test'), description=maison.get('description', ''),
                        image=maison.get('image', ''), lien=maison.get('lien', ''), pays='SN',
                        ville=maison.get('lieu', ''), quartier=maison.get('lieu', ''),
                        superficie=force_to_int(maison.get('superficie', '0')),
                        prix=force_to_int(maison.get('prix', '0')), chambres=force_to_int(maison.get('chambres', '1')),
                        type=maison.get('type', 'rent'),
                        date=datetime.strptime(maison.get('date', "7-8-2018 11:30").replace('.', '-'), '%d-%m-%Y %H:%M').date())
        try:
            m.save()
        except Exception as e:
            print(e)

    for terrain in terrains:
        t = LandAd(titre=terrain.get('titre', 'Annonce'), description=terrain.get('description', ''),
                        image=terrain.get('image', ''), pays='SN',
                        ville=terrain.get('lieu', ''), quartier=terrain.get('lieu', ''),
                   superficie=force_to_int(terrain.get('superficie', '0')),
                        prix=force_to_int(terrain.get('prix', '0')), type=terrain.get('type', 'location'), statut=terrain.get('statut'),
                        date=datetime.strptime(terrain.get('date', "7-8-2018 11:30").replace('.', '-'), '%d-%m-%Y %H:%M').date(),
                         lien=terrain.get('lien', ''), )
        try:
            t.save()
        except Exception as e:
            print(e)

    for job in jobs:
        j = JobAd(titre=job.get('titre', 'Annonce'), description=job.get('description', ''),
                        image=job.get('image', ''), lien=job.get('lien', ''), pays='SN',
                        ville=job.get('lieu', ''), domaines=job.get('lieu', ''),
                        salaire=job.get('salaire', 0), type=job.get('type', 'location'),
                        date=datetime.strptime(job.get('date', "7-8-2018 11:30").replace('.', '-'), '%d-%m-%Y %H:%M').date())
        try:
            j.save()
        except Exception as e:
            print(e)

if __name__ == '__main__':
    #delete_records()
    insert_records()