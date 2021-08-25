import requests
from .models import Region, State, City


__version__ = '0.0.5'


default_app_config = 'djangoaddressesapp.apps.DefaultApp'


def import_regions():
    """
    docstring
    """

    response = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/regioes')
    data = response.json()

    for item in data:
        region = Region()
        region.pk = item.get("id")
        region.name = item.get("nome")
        region.acronym = item.get("sigla")
        region.save()


def import_state():
    """
    docstring
    """

    response = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/estados')
    data = response.json()

    for item in data:
        state = State()
        state.pk = item.get("id")
        state.name = item.get("nome")
        state.acronym = item.get("sigla")
        state.region = Region.objects.get(pk=item.get("regiao").get("id"))
        state.save()


def import_cities():
    """
    docstring
    """

    response = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/municipios')
    data = response.json()

    for item in data:
        city = City()
        city.pk = item.get("id")
        city.name = item.get("nome")
        city.state = State.objects.get(pk=item.get("microrregiao").get("mesorregiao").get("UF").get("id"))
        city.save()
