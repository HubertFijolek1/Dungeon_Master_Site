from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Character, Monster
from django.contrib.auth import get_user_model

User = get_user_model()

class CharacterModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.character = Character.objects.create(name='Test Character', character_type='player', campaign_id=1)

    def test_character_creation(self):
        self.assertEqual(self.character.name, 'Test Character')
        self.assertEqual(self.character.character_type, 'player')

class MonsterModelTest(TestCase):
    def setUp(self):
        self.monster = Monster.objects.create(name='Test Monster')

    def test_monster_creation(self):
        self.assertEqual(self.monster.name, 'Test Monster')

class CharacterAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.character = Character.objects.create(name='API Character', campaign_id=1)

    def test_get_character_list(self):
        response = self.client.get(reverse('character_list'))
        self.assertEqual(response.status_code, 200)

    def test_create_character(self):
        data = {'name': 'New API Character', 'campaign': 1}
        response = self.client.post(reverse('characters-api-list'), data)
        self.assertEqual(response.status_code, 201)