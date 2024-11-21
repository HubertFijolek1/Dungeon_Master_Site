from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from rest_framework import viewsets, permissions
from .models import Character, InventoryItem, Monster
from .serializers import CharacterSerializer, InventoryItemSerializer, MonsterSerializer
from .forms import CharacterForm, InventoryItemForm, MonsterForm
from campaigns.models import Campaign

# REST Framework ViewSets

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class MonsterViewSet(viewsets.ModelViewSet):
    queryset = Monster.objects.all()
    serializer_class = MonsterSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Django Views

class CharacterListView(ListView):
    model = Character
    template_name = 'characters/character_list.html'
    context_object_name = 'characters'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q', '')
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)
        return queryset

class CharacterDetailView(DetailView):
    model = Character
    template_name = 'characters/character_detail.html'
    context_object_name = 'character'

class CharacterCreateView(LoginRequiredMixin, CreateView):
    model = Character
    form_class = CharacterForm
    template_name = 'characters/character_form.html'

    def form_valid(self, form):
        campaign_id = self.kwargs.get('campaign_id')
        form.instance.campaign = get_object_or_404(Campaign, id=campaign_id)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('characters:character_detail', kwargs={'pk': self.object.pk})

class InventoryItemListView(ListView):
    model = InventoryItem
    template_name = 'characters/inventoryitem_list.html'
    context_object_name = 'inventory_items'

    def get_queryset(self):
        character_id = self.kwargs['character_id']
        self.character = get_object_or_404(Character, pk=character_id)
        return InventoryItem.objects.filter(character=self.character)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['character'] = self.character
        return context

class InventoryItemCreateView(LoginRequiredMixin, CreateView):
    model = InventoryItem
    form_class = InventoryItemForm
    template_name = 'characters/inventoryitem_form.html'

    def form_valid(self, form):
        character_id = self.kwargs['character_id']
        form.instance.character = get_object_or_404(Character, pk=character_id)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('inventoryitem_list', kwargs={'character_id': self.object.character.pk})

class MonsterListView(ListView):
    model = Monster
    template_name = 'characters/monster_list.html'
    context_object_name = 'monsters'

    def get_queryset(self):
        queryset = super().get_queryset()
        campaign_id = self.kwargs.get('campaign_id')
        if campaign_id:
            queryset = queryset.filter(campaign_id=campaign_id)
        search_query = self.request.GET.get('q', '')
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)
        return queryset

class MonsterDetailView(DetailView):
    model = Monster
    template_name = 'characters/monster_detail.html'
    context_object_name = 'monster'

class MonsterCreateView(LoginRequiredMixin, CreateView):
    model = Monster
    form_class = MonsterForm
    template_name = 'characters/monster_form.html'

    def form_valid(self, form):
        campaign_id = self.kwargs.get('campaign_id')
        if campaign_id:
            form.instance.campaign = get_object_or_404(Campaign, id=campaign_id)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('monster_detail', kwargs={'pk': self.object.pk})

class CharacterDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'characters/character_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        campaign_id = self.kwargs.get('campaign_id')
        context['campaign'] = get_object_or_404(Campaign, id=campaign_id)
        context['characters'] = Character.objects.filter(campaign_id=campaign_id)
        return context
