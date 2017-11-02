from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Telefono(models.Model):
    """docstring for telefono"""
    id_persona = models.ForeignKey(User)
    tel = models.IntegerField(null=True, blank=True)
