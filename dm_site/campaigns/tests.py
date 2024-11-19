from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Campaign

User = get_user_model()

class CampaignModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.campaign = Campaign.objects.create(
            name='Test Campaign',
            description='A test campaign',
            owner=self.user,
            status='active'
        )

    def test_campaign_creation(self):
        self.assertEqual(self.campaign.name, 'Test Campaign')
        self.assertEqual(self.campaign.owner.username, 'testuser')
        self.assertEqual(self.campaign.status, 'active')

class CampaignViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')
        self.campaign = Campaign.objects.create(
            name='Test Campaign',
            description='A test campaign',
            owner=self.user,
            status='active'
        )

    def test_campaign_list_view(self):
        response = self.client.get(reverse('campaign_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Campaign')

    def test_campaign_detail_view(self):
        response = self.client.get(reverse('campaign_detail', args=[self.campaign.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'A test campaign')

    def test_campaign_create_view(self):
        response = self.client.post(reverse('campaign_create'), {
            'name': 'New Campaign',
            'description': 'A new campaign',
            'status': 'active',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Campaign.objects.last().name, 'New Campaign')
