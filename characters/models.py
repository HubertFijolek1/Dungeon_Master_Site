from django.db import models
from django.conf import settings
from campaigns.models import Campaign

class Character(models.Model):
    CHARACTER_TYPE_CHOICES = [
        ('player', 'Player'),
        ('npc', 'NPC'),
    ]

    name = models.CharField(max_length=255)
    character_type = models.CharField(max_length=10, choices=CHARACTER_TYPE_CHOICES, default='player')
    attributes = models.JSONField(default=dict, blank=True)
    backstory = models.TextField(blank=True)
    campaign = models.ForeignKey('campaigns.Campaign', on_delete=models.CASCADE, related_name='characters')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.get_character_type_display()})"

class Monster(models.Model):
    name = models.CharField(max_length=255)
    stats = models.JSONField(default=dict, blank=True)
    lore = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class InventoryItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    quantity = models.PositiveIntegerField(default=1)
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='inventory_items')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} x{self.quantity} ({self.character.name})"
