from django.contrib import admin
from streamer import models

@admin.register(models.Stream)
class StreamAdmin(admin.ModelAdmin):
    list_display = ['user', 'started_on']
    readonly_fields = ['stream_url']