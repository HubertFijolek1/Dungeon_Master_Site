from rest_framework import viewsets, permissions
from .models import DiceRoll, Encounter, Loot
from .serializers import DiceRollSerializer, EncounterSerializer, LootSerializer
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import EncounterForm, LootForm

class EncounterCreateView(LoginRequiredMixin, CreateView):
    model = Encounter
    form_class = EncounterForm
    template_name = 'mechanics/encounter_form.html'

    def form_valid(self, form):
        form.instance.campaign = self.request.user.campaigns.first()  # Adjust as needed
        response = super().form_valid(form)
        # Implement logic to calculate difficulty based on selected monsters
        self.object.difficulty = self.calculate_difficulty(self.object.monsters.all())
        self.object.save()
        return response

    def calculate_difficulty(self, monsters):
        # Placeholder logic
        total_cr = sum(monster.challenge_rating for monster in monsters)
        if total_cr < 5:
            return 'easy'
        elif total_cr < 10:
            return 'medium'
        elif total_cr < 15:
            return 'hard'
        else:
            return 'deadly'

# Loot Views
class LootListView(ListView):
    model = Loot
    template_name = 'mechanics/loot_list.html'
    context_object_name = 'loot_items'

class LootDetailView(DetailView):
    model = Loot
    template_name = 'mechanics/loot_detail.html'
    context_object_name = 'loot'

class LootCreateView(LoginRequiredMixin, CreateView):
    model = Loot
    form_class = LootForm
    template_name = 'mechanics/loot_form.html'

    def form_valid(self, form):
        return super().form_valid(form)

# Encounter Views
class EncounterListView(ListView):
    model = Encounter
    template_name = 'mechanics/encounter_list.html'
    context_object_name = 'encounters'

class EncounterDetailView(DetailView):
    model = Encounter
    template_name = 'mechanics/encounter_detail.html'
    context_object_name = 'encounter'

class EncounterCreateView(LoginRequiredMixin, CreateView):
    model = Encounter
    form_class = EncounterForm
    template_name = 'mechanics/encounter_form.html'

    def form_valid(self, form):
        form.instance.campaign = self.request.user.campaigns.first()  # Adjust as needed
        return super().form_valid(form)

class DiceRollViewSet(viewsets.ModelViewSet):
    queryset = DiceRoll.objects.all()
    serializer_class = DiceRollSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class EncounterViewSet(viewsets.ModelViewSet):
    queryset = Encounter.objects.all()
    serializer_class = EncounterSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class LootViewSet(viewsets.ModelViewSet):
    queryset = Loot.objects.all()
    serializer_class = LootSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]