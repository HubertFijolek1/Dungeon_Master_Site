from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Campaign, Session, Milestone, Participant
from .serializers import CampaignSerializer, SessionSerializer, MilestoneSerializer, ParticipantSerializer
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CampaignForm, SessionForm, MilestoneForm, ParticipantInviteForm
from django.shortcuts import get_object_or_404, render, redirect
from django.views import View



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

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q', '')
        status_filter = self.request.GET.get('status', '')
        if search_query:
            queryset = queryset.filter(name__icontains=search_query) | queryset.filter(owner__username__icontains=search_query)
        if status_filter:
            queryset = queryset.filter(status=status_filter)
        return queryset

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

class CampaignUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Campaign
    form_class = CampaignForm
    template_name = 'campaigns/campaign_form.html'

    def test_func(self):
        campaign = self.get_object()
        return self.request.user == campaign.owner


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

class MilestoneListView(ListView):
    model = Milestone
    template_name = 'campaigns/milestone_list.html'
    context_object_name = 'milestones'

    def get_queryset(self):
        self.campaign = get_object_or_404(Campaign, pk=self.kwargs['campaign_id'])
        return Milestone.objects.filter(campaign=self.campaign)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['campaign'] = self.campaign
        return context

class MilestoneDetailView(DetailView):
    model = Milestone
    template_name = 'campaigns/milestone_detail.html'
    context_object_name = 'milestone'

class ParticipantInviteView(LoginRequiredMixin, UserPassesTestMixin, View):
    template_name = 'campaigns/participant_invite.html'

    def get(self, request, campaign_id):
        campaign = get_object_or_404(Campaign, pk=campaign_id)
        form = ParticipantInviteForm(campaign=campaign)
        return render(request, self.template_name, {'form': form, 'campaign': campaign})

    def post(self, request, campaign_id):
        campaign = get_object_or_404(Campaign, pk=campaign_id)
        form = ParticipantInviteForm(request.POST, campaign=campaign)
        if form.is_valid():
            form.save()
            return redirect('campaign_detail', pk=campaign_id)
        return render(request, self.template_name, {'form': form, 'campaign': campaign})

    def test_func(self):
        campaign = get_object_or_404(Campaign, pk=self.kwargs['campaign_id'])
        return self.request.user == campaign.owner

class DMDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'campaigns/dm_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['campaigns'] = Campaign.objects.filter(owner=self.request.user)
        return context