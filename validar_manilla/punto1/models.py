import datetime

from django.db import models
from django.utils import timezone

class Caballista(models.Model):
    hash_caballista = models.CharField(max_length=20)
    punto1 = models.IntegerField(default=0)
    punto2 = models.IntegerField(default=0)
