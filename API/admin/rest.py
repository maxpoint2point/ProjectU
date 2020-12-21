from django.contrib import admin
from API.models import RestHeader, ShopPosition, StockPosition


@admin.register(RestHeader)
class RestHeader(admin.ModelAdmin):
    list_display = ('request_id', 'type', 'send_date', 'date', 'status', 'get_workplace')
    readonly_fields = ['request_id', 'date', 'status', 'send_date', 'message']
    list_filter = ('type', 'status', 'workplace')

    def get_workplace(self, obj):
        return obj.workplace.name

    get_workplace.short_description = 'Рабочее место'


@admin.register(StockPosition)
class StockPosition(admin.ModelAdmin):
    list_display = ('get_alcohol', 'get_fa', 'get_fb', 'quantity', 'get_header',)
    readonly_fields = ('alcohol', 'fa', 'fb', 'quantity', 'header',)

    def get_alcohol(self, obj):
        return obj.alcohol.short_name

    def get_fa(self, obj):
        return obj.fa.reg_id

    def get_fb(self, obj):
        return obj.fb.reg_id

    def get_header(self, obj):
        return obj.header.request_id

    get_alcohol.short_description = 'Алкогольная продукция'
    get_fa.short_description = 'Справка А'
    get_fb.short_description = 'Справка B'
    get_header.short_description = 'Запрос'


@admin.register(ShopPosition)
class ShopPosition(admin.ModelAdmin):
    list_display = ('get_alcohol', 'quantity', 'get_header',)
    readonly_fields = ('alcohol', 'quantity', 'header',)

    def get_alcohol(self, obj):
        return obj.alcohol.short_name

    def get_header(self, obj):
        return obj.header.request_id

    get_alcohol.short_description = 'Алкогольная продукция'
    get_header.short_description = 'Запрос'


