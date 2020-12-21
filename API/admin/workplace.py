from django.contrib import admin
from API.models import Workplace


@admin.register(Workplace)
class Workplace(admin.ModelAdmin):
    list_display = ('name', 'fsrar', 'delete_requests', 'load_ttn', 'disabled', 'request_rest', 'get_ou')
    list_display_links = ('name', 'fsrar',)
    readonly_fields = ('fsrar',)
    list_editable = ('delete_requests', 'load_ttn', 'disabled', 'request_rest')

    def get_ou(self, obj):
        return obj.ou.name

    get_ou.short_description = 'Организация'
