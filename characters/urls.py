from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CharacterViewSet, InventoryItemViewSet, MonsterViewSet,
    CharacterListView, CharacterDetailView, CharacterCreateView,
    InventoryItemListView, InventoryItemCreateView,
    MonsterListView, MonsterDetailView, MonsterCreateView,
    CharacterDashboardView,
)

app_name = 'characters'

router = DefaultRouter()
router.register(r'characters-api', CharacterViewSet)
router.register(r'inventory-items-api', InventoryItemViewSet)
router.register(r'monsters-api', MonsterViewSet)

urlpatterns = [
    # API URLs
    path('api/', include(router.urls)),

    # Character URLs
    path('', CharacterListView.as_view(), name='character_list'),
    path('<int:pk>/', CharacterDetailView.as_view(), name='character_detail'),
    path('create/<int:campaign_id>/', CharacterCreateView.as_view(), name='character_create'),

    # InventoryItem URLs
    path('<int:character_id>/inventory/', InventoryItemListView.as_view(), name='inventoryitem_list'),
    path('<int:character_id>/inventory/add/', InventoryItemCreateView.as_view(), name='inventoryitem_add'),

    # Monster URLs
    path('monsters/', MonsterListView.as_view(), name='monster_list'),
    path('monsters/<int:pk>/', MonsterDetailView.as_view(), name='monster_detail'),
    path('monsters/campaign/<int:campaign_id>/', MonsterListView.as_view(), name='campaign_monster_list'),
    path('monsters/create/<int:campaign_id>/', MonsterCreateView.as_view(), name='monster_create'),

    # Character Dashboard
    path('dashboard/<int:campaign_id>/', CharacterDashboardView.as_view(), name='character_dashboard'),
]
