from django.db import models
from django.urls.base import reverse


class Region(models.Model):

    class Meta:
        verbose_name = 'Região'
        verbose_name_plural = 'Regiões'

    name = models.CharField(
        verbose_name="Nome", 
        max_length=254
    )

    acronym = models.CharField(
        verbose_name="Sigla", 
        max_length=2
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("region_detail", kwargs={"pk": self.pk})