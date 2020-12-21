from django.contrib import admin
from API.models import OU


@admin.register(OU)
class OU(admin.ModelAdmin):
    list_display = ('name', 'inn', 'disabled')
