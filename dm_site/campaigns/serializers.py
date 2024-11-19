from rest_framework import serializers
from .models import Campaign, Session, Milestone, Participant

class CampaignSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Campaign
        fields = '__all__'

class SessionSerializer(serializers.ModelSerializer):
    campaign = serializers.ReadOnlyField(source='campaign.id')

    class Meta:
        model = Session
        fields = '__all__'

class MilestoneSerializer(serializers.ModelSerializer):
    campaign = serializers.ReadOnlyField(source='campaign.id')

    class Meta:
        model = Milestone
        fields = '__all__'

class ParticipantSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    campaign = serializers.ReadOnlyField(source='campaign.id')

    class Meta:
        model = Participant
        fields = '__all__'
