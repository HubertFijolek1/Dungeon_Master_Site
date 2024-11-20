from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CharacterViewSet, InventoryItemViewSet, MonsterViewSet

router = DefaultRouter()
router.register(r'characters', CharacterViewSet)
router.register(r'inventory-items', InventoryItemViewSet)
router.register(r'monsters', MonsterViewSet)

urlpatterns = [
    path('api/', include(router.urls)),

]