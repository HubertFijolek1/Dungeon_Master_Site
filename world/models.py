from django.db import models
from django.utils import timezone


class Map(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='maps/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    map = models.ForeignKey(Map, on_delete=models.CASCADE, related_name='locations')
    coordinates = models.CharField(max_length=100, blank=True)  # Adjust as needed
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Lore(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    related_location = models.ForeignKey(
        Location, on_delete=models.SET_NULL, related_name='lore_entries', null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class TimelineEvent(models.Model):
    date = models.DateField()
    description = models.TextField()
    related_lore = models.ForeignKey(
        Lore, on_delete=models.SET_NULL, related_name='timeline_events', null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Event on {self.date}: {self.description[:50]}"