from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    """docstring for usuario."""
    id_persona = models.OneToOneField(User, related_name='id_persona')
    sexo = models.BooleanField(default=True)
# Create your models here.
