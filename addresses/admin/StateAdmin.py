from django.contrib import admin
from ..models import State

# Register your models here.


@admin.register(State)
class StateAdmin(admin.ModelAdmin):

    list_display = [
        "name",
        "acronym",
        "region",
    ]

    list_display_links = [
        "name",
        "acronym",
        "region",
    ]

    list_filter = [
        "region",
    ]
    
    search_fields = [
        "name",
        "acronym",
    ]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, *args):
        return False

    def has_delete_permission(self, request, *args):
        return False