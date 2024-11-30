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
    receiver = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

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
    options = PollOptionSerializer(many=True)
    total_votes = serializers.IntegerField(source='votes.count', read_only=True)

    class Meta:
        model = Poll
        fields = ['id', 'question', 'campaign', 'created_at', 'updated_at', 'options', 'total_votes']

    def create(self, validated_data):
        options_data = validated_data.pop('options')
        poll = Poll.objects.create(**validated_data)
        for option_data in options_data:
            PollOption.objects.create(poll=poll, **option_data)
        return poll

    def update(self, instance, validated_data):
        options_data = validated_data.pop('options', None)
        instance.question = validated_data.get('question', instance.question)
        instance.save()
        if options_data:
            # Update existing options and create new ones
            for option_data in options_data:
                option_id = option_data.get('id', None)
                if option_id:
                    option = PollOption.objects.get(id=option_id, poll=instance)
                    option.option_text = option_data.get('option_text', option.option_text)
                    option.save()
                else:
                    PollOption.objects.create(poll=instance, **option_data)
        return instance

class PollVoteSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    selected_option = serializers.PrimaryKeyRelatedField(queryset=PollOption.objects.all())

    class Meta:
        model = PollVote
        fields = '__all__'

    def validate(self, data):
        user = self.context['request'].user
        poll = data['poll']
        if PollVote.objects.filter(user=user, poll=poll).exists():
            raise serializers.ValidationError("You have already voted in this poll.")
        return data