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
    coordinates = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name