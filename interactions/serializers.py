from rest_framework import serializers
from .models import Message, ForumPost, Poll, PollOption, PollVote
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    receiver = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = '__all__'

class ForumPostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = ForumPost
        fields = '__all__'

class PollOptionSerializer(serializers.ModelSerializer):
    votes_count = serializers.IntegerField(source='votes.count', read_only=True)

    class Meta:
        model = PollOption
        fields = ['id', 'option_text', 'votes_count']

class PollSerializer(serializers.ModelSerializer):
    options = PollOptionSerializer(many=True, read_only=True)
    total_votes = serializers.IntegerField(source='votes.count', read_only=True)

    class Meta:
        model = Poll
        fields = ['id', 'question', 'campaign', 'created_at', 'updated_at', 'options', 'total_votes']

class PollVoteSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    selected_option = PollOptionSerializer(read_only=True)

    class Meta:
        model = PollVote
        fields = '__all__'