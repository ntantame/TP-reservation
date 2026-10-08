"""Taches 3, 4, 5 (et bonus) : vues de l'API.

A FAIRE :
  - SalleViewSet (ModelViewSet), avec l'action `occupation` (tache 5)
  - ReservationViewSet (ModelViewSet), avec perform_create (tache 3)
"""
from rest_framework import viewsets  # noqa: F401  (a utiliser)

from .models import Reservation, Salle  # noqa: F401  (a utiliser)
from .permissions import IsOwnerOrReadOnly, IsStaffOrReadOnly
from rest_framework.decorators import action
from .serializers import ReservationSerializer, SalleSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# ModelViewSet pour la salle
class SalleViewSet(viewsets.ModelViewSet):
    queryset = Salle.objects.all()
    serializer_class = SalleSerializer
    permission_classes = [IsStaffOrReadOnly]

    @action(detail=True, methods=['post'])
    def occupation(self, request, pk=None):
        salle = self.get_object()



# ModelViewSet pour la reservation
class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    # L'utilisateur est automatiquement l'utilisateur connecte
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# TODO : votre code ici
