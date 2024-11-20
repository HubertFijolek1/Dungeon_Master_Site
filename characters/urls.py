from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CharacterViewSet, InventoryItemViewSet, MonsterViewSet, CharacterListView, CharacterDetailView, CharacterCreateView

router = DefaultRouter()
router.register(r'characters', CharacterViewSet)
router.register(r'inventory-items', InventoryItemViewSet)
router.register(r'monsters', MonsterViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('characters/', CharacterListView.as_view(), name='character_list'),
    path('characters/<int:pk>/', CharacterDetailView.as_view(), name='character_detail'),
    path('characters/create/', CharacterCreateView.as_view(), name='character_create'),

]
