from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Volunteer(models.Model):

    user = models.OneToOneField(User)
    second_last_name = models.CharField(max_length=250)
    calle = models.CharField(max_length=250)
    colonia = models.CharField(max_length=250)
    municipio = models.CharField(max_length=250)
    estado = models.CharField(max_length=250)
    telefono = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Volunteer"
        verbose_name_plural = "Volunteers"

    def __str__(self):
        return self.user
