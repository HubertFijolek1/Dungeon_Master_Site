from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from .models import DiceRoll, Encounter, Loot
from campaigns.models import Campaign
from characters.models import Monster

User = get_user_model()

class DiceRollModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.campaign = Campaign.objects.create(name='Test Campaign')
        self.dice_roll = DiceRoll.objects.create(
            roll_type='custom',
            result='1d20+5 = 15',
            user=self.user,
            campaign=self.campaign
        )

    def test_dice_roll_creation(self):
        self.assertEqual(self.dice_roll.result, '1d20+5 = 15')
        self.assertEqual(self.dice_roll.user, self.user)
        self.assertEqual(self.dice_roll.campaign, self.campaign)

class EncounterModelTest(TestCase):
    def setUp(self):
        self.campaign = Campaign.objects.create(name='Test Campaign')
        self.monster = Monster.objects.create(name='Goblin', challenge_rating=0.25)
        self.encounter = Encounter.objects.create(
            name='Test Encounter',
            campaign=self.campaign
        )
        self.encounter.monsters.add(self.monster)

    def test_encounter_creation(self):
        self.assertEqual(self.encounter.name, 'Test Encounter')
        self.assertIn(self.monster, self.encounter.monsters.all())

class LootModelTest(TestCase):
    def setUp(self):
        self.campaign = Campaign.objects.create(name='Test Campaign')
        self.encounter = Encounter.objects.create(name='Test Encounter', campaign=self.campaign)
        self.loot = Loot.objects.create(
            name='Gold Coins',
            type='gold',
            value=100,
            encounter=self.encounter
        )

    def test_loot_creation(self):
        self.assertEqual(self.loot.name, 'Gold Coins')
        self.assertEqual(self.loot.value, 100)
        self.assertEqual(self.loot.encounter, self.encounter)

class DiceRollAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.campaign = Campaign.objects.create(name='Test Campaign')
        self.client.login(username='testuser', password='password')

    def test_create_dice_roll(self):
        data = {'roll_type': 'custom', 'result': '1d6 = 4', 'campaign': self.campaign.id}
        response = self.client.post(reverse('mechanics:diceroll-list'), data)
        self.assertEqual(response.status_code, 201)