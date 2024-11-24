from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    DiceRollViewSet, EncounterViewSet, LootViewSet,
    DiceRollCreateView, DiceRollListView,
    EncounterListView, EncounterDetailView, EncounterCreateView,
    LootListView, LootDetailView, LootCreateView,
)

router = DefaultRouter()
router.register(r'dice-rolls', DiceRollViewSet)
router.register(r'encounters', EncounterViewSet)
router.register(r'loot', LootViewSet)

app_name = 'mechanics'

urlpatterns = [
    # API URLs
    path('api/', include(router.urls)),

    # DiceRoll URLs
    path('dice-rolls/', DiceRollListView.as_view(), name='diceroll_list'),
    path('dice-rolls/roll/', DiceRollCreateView.as_view(), name='diceroll_create'),

    # Encounter URLs
    path('encounters/', EncounterListView.as_view(), name='encounter_list'),
    path('encounters/<int:pk>/', EncounterDetailView.as_view(), name='encounter_detail'),
    path('encounters/create/', EncounterCreateView.as_view(), name='encounter_create'),

    # Loot URLs
    path('loot/', LootListView.as_view(), name='loot_list'),
    path('loot/<int:pk>/', LootDetailView.as_view(), name='loot_detail'),
    path('loot/create/', LootCreateView.as_view(), name='loot_create'),
]