from django.contrib import admin
from .models import Event, FileModel, Reservation


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'time', 'requires_reservation')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('event', 'name', 'email')


@admin.register(FileModel)
class FileAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'description')

