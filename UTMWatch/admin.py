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
    pass


@admin.register(Queue)
class Queue(admin.ModelAdmin):
    pass


@admin.register(StockPosition)
class StockPosition(admin.ModelAdmin):
    pass


@admin.register(FA)
class FA(admin.ModelAdmin):
    pass


@admin.register(FB)
class FB(admin.ModelAdmin):
    pass
