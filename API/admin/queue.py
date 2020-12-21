from django.contrib import admin
from API.models import Queue


@admin.register(Queue)
class Queue(admin.ModelAdmin):
    list_display = ('reply_id', 'status', 'timestamp', 'get_workplace')
    readonly_fields = ('reply_id', 'workplace')

    def get_workplace(self, obj):
        return obj.workplace.name

    get_workplace.short_description = 'Рабочее место'
