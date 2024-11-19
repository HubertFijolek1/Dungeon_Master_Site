from rest_framework.routers import DefaultRouter
from .views import CampaignViewSet, SessionViewSet, MilestoneViewSet

router = DefaultRouter()
router.register(r'campaigns', CampaignViewSet, basename='campaign')
router.register(r'sessions', SessionViewSet, basename='session')
router.register(r'milestones', MilestoneViewSet, basename='milestone')

urlpatterns = router.urls