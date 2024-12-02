from django.db import models

class Spell(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    level = models.PositiveIntegerField()
    SCHOOL_CHOICES = [
        ('Abjuration', 'Abjuration'),
        ('Conjuration', 'Conjuration'),
        ('Divination', 'Divination'),
        ('Enchantment', 'Enchantment'),
        ('Evocation', 'Evocation'),
        ('Illusion', 'Illusion'),
        ('Necromancy', 'Necromancy'),
        ('Transmutation', 'Transmutation'),
    ]
    school = models.CharField(max_length=50, choices=SCHOOL_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} (Level {self.level})"

class Ability(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    TYPE_CHOICES = [
        ('Passive', 'Passive'),
        ('Active', 'Active'),
        ('Reaction', 'Reaction'),
    ]
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    related_spell = models.ForeignKey(Spell, on_delete=models.SET_NULL, null=True, blank=True, related_name='abilities')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name