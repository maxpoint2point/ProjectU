from django.contrib import admin
from API.models import Alcohol, VCode


@admin.register(VCode)
class VCode(admin.ModelAdmin):
    list_display = ('vcode', 'name')
    list_display_links = list_display
    readonly_fields = ('vcode',)


@admin.register(Alcohol)
class Alcohol(admin.ModelAdmin):
    list_display = ('reg_id', 'short_name', 'get_vcode', 'get_producer')
    list_display_links = list_display
    readonly_fields = ('reg_id', 'full_name', 'short_name', 'capacity', 'volume', 'v_code', 'producer',)
    search_fields = ('reg_id', 'short_name', 'full_name', 'producer__full_name', 'producer__short_name')

    def get_producer(self, obj):
        return obj.producer.short_name

    def get_vcode(self, obj):
        return obj.v_code.name

    get_vcode.short_description = 'Вид'
    get_producer.short_description = 'Производитель'
