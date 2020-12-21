from django.contrib import admin
from API.models import Producer


@admin.register(Producer)
class Producer(admin.ModelAdmin):
    list_display = ('reg_id', 'short_name', 'inn', 'kpp',)
    list_display_links = list_display
    readonly_fields = ('reg_id', 'full_name', 'short_name', 'inn', 'kpp', 'country', 'region_code', 'address',)
