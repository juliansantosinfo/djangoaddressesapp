from django.db import models
from django.urls.base import reverse


class State(models.Model):

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

    name = models.CharField(
        verbose_name="Nome", 
        max_length=254
    )

    acronym = models.CharField(
        verbose_name="Sigla", 
        max_length=2
    )

    region = models.ForeignKey(
        "Region", 
        verbose_name="Região", 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("state_detail", kwargs={"pk": self.pk})
