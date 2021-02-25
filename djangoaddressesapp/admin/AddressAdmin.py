from django.contrib import admin
from ..models import Address

# Register your models here.


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):

    list_display = [
        "zipcode",
        "state",
        "city",
        "district",
        "address",
        "number",
    ]

    list_display_links = [
        "zipcode",
        "state",
        "city",
        "district",
        "address",
        "number",
    ]
    
    search_fields = [
        "zipcode",
        "state__name",
        "city__name",
        "district",
        "address",
        "number",
    ]

    autocomplete_fields = [
        "state",
        "city",
    ]
