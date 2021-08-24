import requests
from django.core.management.base import BaseCommand, CommandError
from djangoaddressesapp import import_regions, import_state, import_cities

class Command(BaseCommand):
    help = 'Import regions, states and cities by IBGE api'

    def handle(self, *args, **options):
        
        # Import Regions
        self.stdout.write(self.style.NOTICE('Initializing regions import by IBGE api.'))
        import_regions()
        self.stdout.write(self.style.SUCCESS('Completed regions import by IBGE api.'))

        # Import States
        self.stdout.write(self.style.NOTICE('Initializing states import by IBGE api.'))
        import_state()
        self.stdout.write(self.style.SUCCESS('Completed cities import by IBGE api.'))

        # Import Cities
        self.stdout.write(self.style.NOTICE('Initializing states import by IBGE api.'))
        import_cities()
        self.stdout.write(self.style.SUCCESS('Completed cities import by IBGE api.'))
