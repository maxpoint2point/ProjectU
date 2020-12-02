from django.contrib import admin
from API.models import *


@admin.register(OU)
class OU(admin.ModelAdmin):
    list_display = ('name', 'inn', 'disabled')


@admin.register(Workplace)
class Workplace(admin.ModelAdmin):
    list_display = ('name', 'fsrar', 'delete_requests', 'load_ttn', 'disabled', 'get_ou')
    list_display_links = ('name', 'fsrar',)
    readonly_fields = ('fsrar',)
    list_editable = ('delete_requests', 'load_ttn', 'disabled',)

    def get_ou(self, obj):
        return obj.ou.name

    get_ou.short_description = 'Организация'


@admin.register(RestHeader)
class RestHeader(admin.ModelAdmin):
    list_display = ('request_id', 'type', 'send_date', 'date', 'status', 'get_workplace')
    readonly_fields = ['request_id', 'type', 'date', 'status', 'send_date', 'message', 'workplace']
    list_filter = ('type', 'status', 'workplace')

    def get_workplace(self, obj):
        return obj.workplace.name

    get_workplace.short_description = 'Рабочее место'


@admin.register(Queue)
class Queue(admin.ModelAdmin):
    list_display = ('reply_id', 'status', 'timestamp', 'get_workplace')
    readonly_fields = ('reply_id', 'workplace')

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


@admin.register(FA)
class FA(admin.ModelAdmin):
    readonly_fields = ('reg_id',)


@admin.register(FB)
class FB(admin.ModelAdmin):
    readonly_fields = ('reg_id',)


@admin.register(VCode)
class VCode(admin.ModelAdmin):
    list_display = ('vcode', 'name')
    list_display_links = list_display
    readonly_fields = ('vcode',)


@admin.register(Producer)
class Producer(admin.ModelAdmin):
    list_display = ('reg_id', 'short_name', 'inn', 'kpp',)
    list_display_links = list_display
    readonly_fields = ('reg_id', 'full_name', 'short_name', 'inn', 'kpp', 'country', 'region_code', 'address',)


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


@admin.register(Ticket)
class Ticket(admin.ModelAdmin):
    pass


@admin.register(WayBillList)
class WayBillList(admin.ModelAdmin):
    pass


@admin.register(WayBillData)
class WayBillData(admin.ModelAdmin):
    pass
