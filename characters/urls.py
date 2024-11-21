from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CharacterViewSet, InventoryItemViewSet, MonsterViewSet,
    CharacterListView, CharacterDetailView, CharacterCreateView,
    InventoryItemListView, InventoryItemCreateView,
    MonsterListView, MonsterDetailView, MonsterCreateView,
    CharacterDashboardView,
)

router = DefaultRouter()
router.register(r'characters-api', CharacterViewSet)
router.register(r'inventory-items-api', InventoryItemViewSet)
router.register(r'monsters-api', MonsterViewSet)

urlpatterns = [
    # API URLs
    path('api/', include(router.urls)),

    # Character URLs
    path('characters/', CharacterListView.as_view(), name='character_list'),
    path('characters/<int:pk>/', CharacterDetailView.as_view(), name='character_detail'),
    path('campaigns/<int:campaign_id>/characters/create/', CharacterCreateView.as_view(), name='character_create'),

    # InventoryItem URLs
    path('characters/<int:character_id>/inventory/', InventoryItemListView.as_view(), name='inventoryitem_list'),
    path('characters/<int:character_id>/inventory/add/', InventoryItemCreateView.as_view(), name='inventoryitem_add'),

    # Monster URLs
    path('monsters/', MonsterListView.as_view(), name='monster_list'),
    path('monsters/<int:pk>/', MonsterDetailView.as_view(), name='monster_detail'),
    path('campaigns/<int:campaign_id>/monsters/', MonsterListView.as_view(), name='campaign_monster_list'),
    path('campaigns/<int:campaign_id>/monsters/create/', MonsterCreateView.as_view(), name='monster_create'),

    # Character Dashboard
    path('campaigns/<int:campaign_id>/characters/dashboard/', CharacterDashboardView.as_view(), name='character_dashboard'),
]
