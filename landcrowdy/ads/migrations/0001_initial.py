# Generated by Django 2.1 on 2018-08-17 16:19

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Annonce',
            fields=[
                ('uuid', models.UUIDField(db_index=True, default=uuid.UUID('b404625d-e85a-4464-8de2-86ef51d949f8'), editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(default='Nouvelle annonce', max_length=250)),
                ('description', models.TextField(blank=True)),
                ('source', models.CharField(max_length=250)),
                ('link', models.CharField(max_length=250)),
                ('image', models.CharField(blank=True, max_length=250)),
                ('country', models.CharField(choices=[('CI', "Côte d'Ivoire"), ('CM', 'Caméroun'), ('GH', 'Ghana'), ('KE', 'Kenya'), ('MA', 'Maroc'), ('NG', 'Nigéria'), ('SN', 'Sénégal'), ('TN', 'Tunisie')], default='SN', max_length=2)),
                ('location', models.CharField(blank=True, max_length=250)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='HousingAd',
            fields=[
                ('annonce_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ads.Annonce')),
                ('surface_area', models.IntegerField(blank=True)),
                ('price', models.IntegerField(blank=True)),
                ('rooms', models.IntegerField(blank=True)),
                ('ad_type', models.CharField(choices=[('Housing', 'Logement')], default='Housing', max_length=20)),
                ('housing_type', models.CharField(choices=[('House', 'Maison'), ('Flat', 'Appartement')], default='Flat', max_length=20)),
                ('transaction_type', models.CharField(choices=[('buy', 'Vente'), ('rent', 'Location')], default='rent', max_length=20)),
            ],
            bases=('ads.annonce',),
        ),
        migrations.CreateModel(
            name='JobAd',
            fields=[
                ('annonce_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ads.Annonce')),
                ('ad_type', models.CharField(choices=[('Job', 'Emploi')], default='Job', max_length=20)),
                ('subjects', models.CharField(blank=True, max_length=250)),
                ('gross_salary', models.IntegerField(blank=True)),
                ('contract_type', models.CharField(choices=[('CDI', 'CDI'), ('CDD', 'CDD'), ('Undefined', 'Non précisé')], default='Undefined', max_length=20)),
            ],
            bases=('ads.annonce',),
        ),
        migrations.CreateModel(
            name='LandAd',
            fields=[
                ('annonce_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ads.Annonce')),
                ('surface_area', models.IntegerField(blank=True)),
                ('price', models.IntegerField(blank=True)),
                ('status', models.CharField(choices=[('Approved', 'Titré'), ('Not Approved', 'Non Titré')], default='Approved', max_length=20)),
                ('ad_type', models.CharField(choices=[('land', 'Terrain')], default='Land', max_length=20)),
                ('transaction_type', models.CharField(choices=[('buy', 'Vente'), ('rent', 'Location')], default='rent', max_length=20)),
            ],
            bases=('ads.annonce',),
        ),
    ]
