import logging

from django.conf import settings
from django.db import models
from django.urls import reverse

logger = logging.getLogger(__name__)

class {{ app_name|capfirst }}(models.Model):
    Alege{{ app_name|capfirst }} = models.IntegerChoices(
        ('unu', 'Varianta unu'),
        ('doi', 'Varianta doi'),
    )

    alegere = models.IntegerField(
        verbose_name=("Alege"), choices=Alege{{ app_name|capfirst }}.choices, default=Alege{{ app_name|capfirst }}.unu
    )
    nume = models.CharField(verbose_name=("Nume"), max_length=255, blank=True, null=True, default="")
    descriere_privata = models.TextField(verbose_name=("Descriere privată"), null=True, blank=True, default="")
    soft_delete = models.BooleanField(verbose_name=("Ascunde"), default=False)
    creat = models.DateTimeField(verbose_name=("Dată creare"), auto_now_add=True, blank=True)
    actualizat = models.DateTimeField(verbose_name=("Dată actualizare"), auto_now=True)

    class Meta:
        verbose_name = "{{ app_name|capfirst }}"
        verbose_name_plural = "{{ app_name|capfirst }}"
        ordering = [-"pk"]

    def __str__(self):
        return self.nume

    def get_absolute_url(self):
        return reverse("{{ app_name }}:{{ app_name }}", args=[str(self.pk)])
