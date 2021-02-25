from django.db import models
from django.urls.base import reverse
from djangosimplemodels import SimpleAddress


class Address(SimpleAddress):

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    zipcode = models.CharField(
        verbose_name="CEP",
        max_length=8,
        blank=True,
        null=True
    )

    state = models.ForeignKey(
        "State", 
        verbose_name="Estado", 
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    city = models.ForeignKey(
        "City", 
        verbose_name="Município", 
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    district = models.CharField(
        verbose_name="Bairro",
        max_length=254
    )

    address = models.CharField(
        verbose_name="Endereço",
        max_length=254
    )

    number = models.IntegerField(
        verbose_name="Número",
    )

    def __str__(self):
        return self.address

    def get_absolute_url(self):
        return reverse("address_detail", kwargs={"pk": self.pk})
