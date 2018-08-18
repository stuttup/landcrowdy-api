# Generated by Django 2.1 on 2018-08-18 03:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housingad',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.UUID('7aef7ccd-f2dd-4f18-86e7-67705e6d988f'), editable=False),
        ),
        migrations.AlterField(
            model_name='jobad',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.UUID('245f670b-49e9-471a-a0ae-0c89e0d1b5e0'), editable=False),
        ),
        migrations.AlterField(
            model_name='landad',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.UUID('1a531628-80d5-4d5b-bdfe-f0f7616bd72a'), editable=False),
        ),
    ]
