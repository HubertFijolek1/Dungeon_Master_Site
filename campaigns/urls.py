from django.urls import path
from .views import (
    CampaignListView, CampaignDetailView, CampaignCreateView, CampaignUpdateView,
    SessionListView, SessionDetailView,
    MilestoneListView, MilestoneDetailView,
    ParticipantInviteView,
)

app_name = 'campaigns'

urlpatterns = [
    path('', CampaignListView.as_view(), name='campaign_list'),
    path('<int:pk>/', CampaignDetailView.as_view(), name='campaign_detail'),
    path('create/', CampaignCreateView.as_view(), name='campaign_create'),
    path('<int:pk>/edit/', CampaignUpdateView.as_view(), name='campaign_edit'),
    path('<int:campaign_id>/sessions/', SessionListView.as_view(), name='session_list'),
    path('<int:campaign_id>/sessions/<int:pk>/', SessionDetailView.as_view(), name='session_detail'),
    path('<int:campaign_id>/milestones/', MilestoneListView.as_view(), name='milestone_list'),
    path('<int:campaign_id>/milestones/<int:pk>/', MilestoneDetailView.as_view(), name='milestone_detail'),
    path('<int:campaign_id>/invite/', ParticipantInviteView.as_view(), name='participant_invite'),
]
