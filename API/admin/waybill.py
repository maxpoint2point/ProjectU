from django.contrib import admin
from API.models import WayBillData, WayBillList


@admin.register(WayBillList)
class WayBillList(admin.ModelAdmin):
    pass


@admin.register(WayBillData)
class WayBillData(admin.ModelAdmin):
    pass
