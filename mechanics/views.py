from rest_framework import viewsets, permissions
from .models import DiceRoll, Encounter, Loot
from .serializers import DiceRollSerializer, EncounterSerializer, LootSerializer
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import EncounterForm

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