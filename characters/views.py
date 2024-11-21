from rest_framework import viewsets, permissions
from .models import Character, InventoryItem, Monster
from .serializers import CharacterSerializer, InventoryItemSerializer, MonsterSerializer
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CharacterForm, InventoryItemForm

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
        form.instance.campaign_id = self.kwargs['campaign_id']
        return super().form_valid(form)

class InventoryItemListView(ListView):
    model = InventoryItem
    template_name = 'characters/inventoryitem_list.html'
    context_object_name = 'inventory_items'

    def get_queryset(self):
        return InventoryItem.objects.filter(character_id=self.kwargs['character_id'])

class InventoryItemCreateView(LoginRequiredMixin, CreateView):
    model = InventoryItem
    form_class = InventoryItemForm
    template_name = 'characters/inventoryitem_form.html'

    def form_valid(self, form):
        form.instance.character_id = self.kwargs['character_id']
        return super().form_valid(form)

class CharacterDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'characters/character_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        campaign_id = self.kwargs.get('campaign_id')
        context['campaign'] = get_object_or_404(Campaign, id=campaign_id)
        context['characters'] = Character.objects.filter(campaign_id=campaign_id)
        return context