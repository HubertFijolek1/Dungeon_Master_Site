from rest_framework import viewsets, permissions
from .models import DiceRoll, Encounter, Loot
from .serializers import DiceRollSerializer, EncounterSerializer, LootSerializer
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import EncounterForm, LootForm
import random
from django.urls import reverse_lazy
from django.contrib import messages
import re

class DiceRollCreateView(LoginRequiredMixin, CreateView):
    form_class = DiceRollForm
    template_name = 'mechanics/diceroll_form.html'

    def form_valid(self, form):
        expression = form.cleaned_data['expression']
        result = self.parse_dice_expression(expression)
        if result is not None:
            DiceRoll.objects.create(
                roll_type=form.cleaned_data['roll_type'],
                result=f"{expression} = {result}",
                user=self.request.user,
                campaign=self.request.user.campaigns.first(),  # Adjust as needed
            )
            messages.success(self.request, f"Roll result: {result}")
            return super().form_valid(form)
        else:
            form.add_error('expression', 'Invalid dice expression.')
            return self.form_invalid(form)

    def parse_dice_expression(self, expression):
        # Simple dice expression parser (e.g., '1d20+5')
        dice_pattern = re.compile(r'(\d*)d(\d+)([+-]\d+)?')
        match = dice_pattern.fullmatch(expression.replace(' ', ''))
        if match:
            num_dice = int(match.group(1) or 1)
            dice_sides = int(match.group(2))
            modifier = int(match.group(3) or 0)
            total = sum(random.randint(1, dice_sides) for _ in range(num_dice)) + modifier
            return total
        return None

    def get_success_url(self):
        return reverse_lazy('mechanics:diceroll_list')

class DiceRollListView(ListView):
    model = DiceRoll
    template_name = 'mechanics/diceroll_list.html'
    context_object_name = 'dice_rolls'

    def get_queryset(self):
        return DiceRoll.objects.filter(user=self.request.user)

class EncounterCreateView(LoginRequiredMixin, CreateView):
    model = Encounter
    form_class = EncounterForm
    template_name = 'mechanics/encounter_form.html'

    def form_valid(self, form):
        form.instance.campaign = self.request.user.campaigns.first()  # Adjust as needed
        response = super().form_valid(form)
        # Calculate difficulty
        self.object.difficulty = self.calculate_difficulty(self.object.monsters.all())
        self.object.save()
        # Generate loot
        self.generate_loot(self.object)
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

    def generate_loot(self, encounter):
        loot_types = {
            'easy': [('gold', 50), ('potion', 1)],
            'medium': [('gold', 100), ('weapon', 1)],
            'hard': [('gold', 200), ('armor', 1), ('potion', 2)],
            'deadly': [('gold', 500), ('weapon', 2), ('armor', 2), ('potion', 3)],
        }
        for loot_type, quantity in loot_types.get(encounter.difficulty, []):
            for _ in range(quantity):
                Loot.objects.create(
                    name=f"Generated {loot_type.capitalize()}",
                    type=loot_type,
                    value=random.randint(10, 100),
                    encounter=encounter
                )

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