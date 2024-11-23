from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Map, Location, Lore, TimelineEvent

class MapModelTest(TestCase):
    def setUp(self):
        self.map = Map.objects.create(name='Test Map')

    def test_map_creation(self):
        self.assertEqual(self.map.name, 'Test Map')
        self.assertTrue(isinstance(self.map, Map))

class LocationModelTest(TestCase):
    def setUp(self):
        self.map = Map.objects.create(name='Test Map')
        self.location = Location.objects.create(name='Test Location', map=self.map, coordinates='0,0')

    def test_location_creation(self):
        self.assertEqual(self.location.name, 'Test Location')
        self.assertEqual(self.location.map, self.map)
        self.assertTrue(isinstance(self.location, Location))

class LoreModelTest(TestCase):
    def setUp(self):
        self.location = Location.objects.create(name='Test Location')
        self.lore = Lore.objects.create(title='Test Lore', content='Some content', related_location=self.location)

    def test_lore_creation(self):
        self.assertEqual(self.lore.title, 'Test Lore')
        self.assertEqual(self.lore.related_location, self.location)
        self.assertTrue(isinstance(self.lore, Lore))

class TimelineEventModelTest(TestCase):
    def setUp(self):
        self.lore = Lore.objects.create(title='Test Lore', content='Some content')
        self.event = TimelineEvent.objects.create(date='2023-01-01', description='An event', related_lore=self.lore)

    def test_timeline_event_creation(self):
        self.assertEqual(self.event.description, 'An event')
        self.assertEqual(self.event.related_lore, self.lore)
        self.assertTrue(isinstance(self.event, TimelineEvent))

class MapAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.map = Map.objects.create(name='API Map')

    def test_get_map_list(self):
        response = self.client.get(reverse('world:map-list'))
        self.assertEqual(response.status_code, 200)

    def test_create_map(self):
        data = {'name': 'New API Map'}
        response = self.client.post(reverse('world:map-list'), data)
        self.assertEqual(response.status_code, 201)