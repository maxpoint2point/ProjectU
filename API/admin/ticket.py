from django.contrib import admin
from API.models import Ticket


@admin.register(Ticket)
class Ticket(admin.ModelAdmin):
    pass
