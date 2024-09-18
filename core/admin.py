from django.contrib import admin
from .models import Event, FileModel


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'time')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(FileModel)
class FileAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'description')

