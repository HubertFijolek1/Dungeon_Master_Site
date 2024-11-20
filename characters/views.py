from rest_framework import viewsets, permissions
from .models import Character, InventoryItem, Monster
from .serializers import CharacterSerializer, InventoryItemSerializer, MonsterSerializer
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CharacterForm

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()

class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class MonsterViewSet(viewsets.ModelViewSet):
    queryset = Monster.objects.all()
    serializer_class = MonsterSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CharacterListView(ListView):
    model = Character
    template_name = 'characters/character_list.html'
    context_object_name = 'characters'

class CharacterDetailView(DetailView):
    model = Character
    template_name = 'characters/character_detail.html'
    context_object_name = 'character'

class CharacterCreateView(LoginRequiredMixin, CreateView):
    model = Character
    form_class = CharacterForm
    template_name = 'characters/character_form.html'

    def form_valid(self, form):
        return super().form_valid(form)