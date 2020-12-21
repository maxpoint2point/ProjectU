from django.contrib import admin
from API.models import FA, FB


@admin.register(FA)
class FA(admin.ModelAdmin):
    readonly_fields = ('reg_id',)


@admin.register(FB)
class FB(admin.ModelAdmin):
    readonly_fields = ('reg_id',)
