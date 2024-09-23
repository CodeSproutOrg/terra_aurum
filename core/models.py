from django.db import models
from django.utils.text import slugify
from terra_aurum.settings import FILES_DIR, EVENTS_FOTO_DIR


class Event(models.Model):
    photo = models.ImageField(
        blank=True, null=True,
        upload_to=EVENTS_FOTO_DIR,
        default=f'{EVENTS_FOTO_DIR}/default.jpg'
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    time = models.DateTimeField()
    slug = models.SlugField(unique=True)

    # Reservation system
    requires_reservation = models.BooleanField(default=False)
    total_tickets = models.PositiveIntegerField(default=0)
    available_tickets = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.title} {self.time.date()}")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Reservation(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='reservations')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    tickets = models.PositiveIntegerField()
    reserved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Reservation for {self.name} - {self.event.title}'


class FileModel(models.Model):
    file_name = models.CharField(max_length=200)
    file = models.FileField(upload_to=FILES_DIR)
    description = models.TextField()

    def __str__(self):
        dir_name = self.file.name.split('.')[0]
        name = dir_name.split('/')[-1]
        return name
