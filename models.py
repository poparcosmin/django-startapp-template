import logging
from django.conf import settings
from django.db import models
from django.urls import reverse

logger = logging.getLogger(__name__)


class {{ app_name|capfirst }}Manager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(soft_delete=True)


class {{ app_name|capfirst }}(models.Model):
    CHOICES = models.IntegerChoices(
        ('unu', 'Varianta unu'),
        ('doi', 'Varianta doi'),
    )

    alegere = models.IntegerField(
        verbose_name=("Alege"), choices=CHOICES.choices, default=CHOICES.unu
    )
    nume = models.CharField(verbose_name=("Nume"), max_length=255, blank=True, null=True, default="")
    descriere_privata = models.TextField(verbose_name=("Descriere privată"), null=True, blank=True, default="")
    soft_delete = models.BooleanField(verbose_name=("Ascunde"), default=False)
    creat = models.DateTimeField(verbose_name=("Dată creare"), auto_now_add=True, blank=True)
    actualizat = models.DateTimeField(verbose_name=("Dată actualizare"), auto_now=True)

    objects = models.Manager()
    visible_objects = {{ app_name|capfirst }}Manager()

    class Meta:
        verbose_name = "{{ app_name|capfirst }}"
        verbose_name_plural = "{{ app_name|capfirst }}"
        ordering = ['-pk']

    def __str__(self):
        return self.nume

    def get_absolute_url(self):
        return reverse("{{ app_name }}:detail", args=[str(self.pk)])

    def save(self, *args, **kwargs):
        # override the save method to ensure soft_delete is False when an object is saved
        if self.soft_delete:
            self.soft_delete = False
        super().save(*args, **kwargs)

    ### metode pentru url slug
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super().save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse("{{ app_name }}:detail", args=[str(self.slug)])
