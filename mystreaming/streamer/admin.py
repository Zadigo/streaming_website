from django.contrib import admin
from streamer import models

@admin.register(models.Stream)
class StreamAdmin(admin.ModelAdmin):
    list_display = ['user', 'key', 'started_on', 'is_live']
    readonly_fields = ['stream_url']