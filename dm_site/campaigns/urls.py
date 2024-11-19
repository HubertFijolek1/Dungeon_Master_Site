from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import (
    CampaignListView, CampaignDetailView, CampaignCreateView, CampaignUpdateView,
    SessionListView, SessionDetailView,
    MilestoneListView, MilestoneDetailView,
    ParticipantInviteView,
)

# urlpatterns = [
#     path('', CampaignListView.as_view(), name='campaign_list'),
#     path('campaign/<int:pk>/', CampaignDetailView.as_view(), name='campaign_detail'),
#     path('campaign/create/', CampaignCreateView.as_view(), name='campaign_create'),
#     path('campaign/<int:pk>/edit/', CampaignUpdateView.as_view(), name='campaign_edit'),
#     path('campaign/<int:campaign_id>/sessions/', SessionListView.as_view(), name='session_list'),
#     path('session/<int:pk>/', SessionDetailView.as_view(), name='session_detail'),
#     path('campaign/<int:campaign_id>/milestones/', MilestoneListView.as_view(), name='milestone_list'),
#     path('milestone/<int:pk>/', MilestoneDetailView.as_view(), name='milestone_detail'),
#     path('campaign/<int:campaign_id>/invite/', ParticipantInviteView.as_view(), name='participant_invite'),
# ]

router = DefaultRouter()
router.register(r'campaigns', CampaignViewSet, basename='campaign')
router.register(r'sessions', SessionViewSet, basename='session')
router.register(r'milestones', MilestoneViewSet, basename='milestone')
router.register(r'participants', ParticipantViewSet, basename='participant')

urlpatterns = router.urls