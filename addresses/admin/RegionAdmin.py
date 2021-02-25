from django.contrib import admin
from ..models import Region

# Register your models here.


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):

    list_display = [
        "name",
        "acronym",
    ]

    list_display_links = [
        "name",
        "acronym",
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