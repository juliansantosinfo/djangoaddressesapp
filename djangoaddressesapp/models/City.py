from django.db import models
from django.urls.base import reverse


class City(models.Model):

    class Meta:
        verbose_name = 'Município'
        verbose_name_plural = 'Municípios'

    name = models.CharField(
        verbose_name="Nome", 
        max_length=254
    )

    state = models.ForeignKey(
        "State", 
        verbose_name="", 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("city_detail", kwargs={"pk": self.pk})
