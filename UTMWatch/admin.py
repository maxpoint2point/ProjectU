from django.contrib import admin
from UTMWatch.models import *


@admin.register(OU)
class OU(admin.ModelAdmin):
    pass


@admin.register(Workplace)
class Workplace(admin.ModelAdmin):
    pass


@admin.register(RestHeader)
class RestHeader(admin.ModelAdmin):
    readonly_fields = ['request_id', 'date', 'status']


@admin.register(Queue)
class Queue(admin.ModelAdmin):
    pass


@admin.register(StockPosition)
class StockPosition(admin.ModelAdmin):
    pass


@admin.register(ShopPosition)
class StockPosition(admin.ModelAdmin):
    pass


@admin.register(FA)
class FA(admin.ModelAdmin):
    pass


@admin.register(FB)
class FB(admin.ModelAdmin):
    pass


@admin.register(VCode)
class VCode(admin.ModelAdmin):
    pass


@admin.register(Producer)
class Producer(admin.ModelAdmin):
    pass


@admin.register(Alcohol)
class Alcohol(admin.ModelAdmin):
    pass


@admin.register(Ticket)
class Ticket(admin.ModelAdmin):
    pass


@admin.register(WayBillList)
class WayBillList(admin.ModelAdmin):
    pass


@admin.register(WayBillData)
class WayBillData(admin.ModelAdmin):
    pass
