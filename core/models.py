from django.db import models
from django.utils.text import slugify


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    time = models.DateTimeField()
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.title} {self.time.date()}")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
