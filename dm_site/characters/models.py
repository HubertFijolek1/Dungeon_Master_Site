from django.db import models
from django.conf import settings

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