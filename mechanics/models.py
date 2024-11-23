from django.db import models
from django.contrib.auth import get_user_model
from campaigns.models import Campaign
from characters.models import Monster

User = get_user_model()

class DiceRoll(models.Model):
    ROLL_TYPES = [
        ('attack', 'Attack'),
        ('damage', 'Damage'),
        ('skill', 'Skill Check'),
        ('save', 'Saving Throw'),
        ('custom', 'Custom'),
    ]

    roll_type = models.CharField(max_length=20, choices=ROLL_TYPES, default='custom')
    result = models.CharField(max_length=50)  # You can use IntegerField if appropriate
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dice_rolls')
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='dice_rolls')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} rolled {self.result} ({self.roll_type})"

class Encounter(models.Model):
    DIFFICULTY_LEVELS = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
        ('deadly', 'Deadly'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_LEVELS, default='medium')
    monsters = models.ManyToManyField(Monster, related_name='encounters')
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='encounters')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Loot(models.Model):
    LOOT_TYPES = [
        ('weapon', 'Weapon'),
        ('armor', 'Armor'),
        ('potion', 'Potion'),
        ('gold', 'Gold'),
        ('misc', 'Miscellaneous'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=50, choices=LOOT_TYPES, default='misc')
    value = models.IntegerField(default=0)
    encounter = models.ForeignKey(Encounter, on_delete=models.CASCADE, related_name='loot_items')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name