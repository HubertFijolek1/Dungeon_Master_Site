from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Campaign, Session, Milestone, Participant
from .serializers import CampaignSerializer, SessionSerializer, MilestoneSerializer, ParticipantSerializer
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CampaignForm, SessionForm
from django.shortcuts import get_object_or_404


class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class MilestoneViewSet(viewsets.ModelViewSet):
    queryset = Milestone.objects.all()
    serializer_class = MilestoneSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CampaignListView(ListView):
    model = Campaign
    template_name = 'campaigns/campaign_list.html'
    context_object_name = 'campaigns'

class CampaignDetailView(DetailView):
    model = Campaign
    template_name = 'campaigns/campaign_detail.html'
    context_object_name = 'campaign'

class CampaignCreateView(LoginRequiredMixin, CreateView):
    model = Campaign
    form_class = CampaignForm
    template_name = 'campaigns/campaign_form.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class CampaignUpdateView(LoginRequiredMixin, UpdateView):
    model = Campaign
    form_class = CampaignForm
    template_name = 'campaigns/campaign_form.html'

    def get_queryset(self):
        return Campaign.objects.filter(owner=self.request.user)


class SessionListView(ListView):
    model = Session
    template_name = 'campaigns/session_list.html'
    context_object_name = 'sessions'

    def get_queryset(self):
        self.campaign = get_object_or_404(Campaign, pk=self.kwargs['campaign_id'])
        return Session.objects.filter(campaign=self.campaign)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['campaign'] = self.campaign
        return context

class SessionDetailView(DetailView):
    model = Session
    template_name = 'campaigns/session_detail.html'
    context_object_name = 'session'