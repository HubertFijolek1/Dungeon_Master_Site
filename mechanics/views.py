from rest_framework import viewsets, permissions
from .models import DiceRoll, Encounter
from .serializers import DiceRollSerializer, EncounterSerializer

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