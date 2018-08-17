from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, db_index=True)
    uuid = models.UUIDField(db_index=True, default=uuid.uuid4(), editable=False, primary_key=True)
