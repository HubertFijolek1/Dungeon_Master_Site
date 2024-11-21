from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Character, Monster

class CharacterModelTest(TestCase):
    def setUp(self):
        self.character = Character.objects.create(name='Test Character')

    def test_character_creation(self):
        self.assertEqual(self.character.name, 'Test Character')

class MonsterModelTest(TestCase):
    def setUp(self):
        self.monster = Monster.objects.create(name='Test Monster')

    def test_monster_creation(self):
        self.assertEqual(self.monster.name, 'Test Monster')

class CharacterAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.character = Character.objects.create(name='API Character')

    def test_get_character_list(self):
        response = self.client.get(reverse('character-list'))
        self.assertEqual(response.status_code, 200)

    def test_create_character(self):
        data = {'name': 'New API Character'}
        response = self.client.post(reverse('character-list'), data)
        self.assertEqual(response.status_code, 201)