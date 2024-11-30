from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from .models import Message, ForumPost, Poll, PollOption, PollVote
from campaigns.models import Campaign

User = get_user_model()

class MessageModelTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password')
        self.user2 = User.objects.create_user(username='user2', password='password')
        self.message = Message.objects.create(
            sender=self.user1,
            receiver=self.user2,
            content='Hello!'
        )

    def test_message_creation(self):
        self.assertEqual(self.message.content, 'Hello!')
        self.assertEqual(self.message.sender, self.user1)
        self.assertEqual(self.message.receiver, self.user2)

class ForumPostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user', password='password')
        self.campaign = Campaign.objects.create(name='Test Campaign')
        self.post = ForumPost.objects.create(
            title='Test Post',
            content='This is a test post.',
            author=self.user,
            campaign=self.campaign
        )

    def test_forum_post_creation(self):
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.author, self.user)
        self.assertEqual(self.post.campaign, self.campaign)