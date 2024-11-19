from rest_framework.routers import DefaultRouter
from .views import CampaignViewSet, SessionViewSet

router = DefaultRouter()
router.register(r'campaigns', CampaignViewSet, basename='campaign')
router.register(r'sessions', SessionViewSet, basename='session')

urlpatterns = router.urls