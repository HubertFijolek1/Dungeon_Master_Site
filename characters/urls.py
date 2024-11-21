from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CharacterViewSet, InventoryItemViewSet, MonsterViewSet, CharacterListView, CharacterDetailView, CharacterCreateView, InventoryItemListView,InventoryItemCreateView

router = DefaultRouter()
router.register(r'characters', CharacterViewSet)
router.register(r'inventory-items', InventoryItemViewSet)
router.register(r'monsters', MonsterViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('characters/', CharacterListView.as_view(), name='character_list'),
    path('characters/<int:pk>/', CharacterDetailView.as_view(), name='character_detail'),
    path('characters/create/', CharacterCreateView.as_view(), name='character_create'),
    path('characters/<int:character_id>/inventory/', InventoryItemListView.as_view(), name='inventoryitem_list'),
    path('characters/<int:character_id>/inventory/add/', InventoryItemCreateView.as_view(), name='inventoryitem_add'),
    path('campaigns/<int:campaign_id>/characters/create/', CharacterCreateView.as_view(), name='character_create'),
    path('campaigns/<int:campaign_id>/characters/dashboard/', CharacterDashboardView.as_view(),
         name='character_dashboard'),

]
