from django.contrib import admin
from ..models import City

# Register your models here.


@admin.register(City)
class CityAdmin(admin.ModelAdmin):

    list_display = [
        "name",
        "state",
    ]

    list_display_links = [
        "name",
        "state",
    ]
    
    list_filter = [
        "state",
        "state__region",
    ]

    search_fields = [
        "name",
        "state__name",
    ]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, *args):
        return False

    def has_delete_permission(self, request, *args):
        return False
