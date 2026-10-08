"""Tache 1 et 2 : serializers et validation.

A FAIRE :
  - SalleSerializer (ModelSerializer)
  - ReservationSerializer (ModelSerializer) :
      * le champ `utilisateur` est en LECTURE SEULE (il sera renseigne par la vue)
      * validation : `fin` strictement apres `debut`
      * validation : pas de chevauchement avec une autre reservation CONFIRMEE
        de la meme salle
"""
from rest_framework import serializers

from .models import Reservation, Salle  # noqa: F401  (a utiliser)
# creation du SalleSerializer
class SalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salle
        fields = ["id", "nom","capacite", "batiment"]

# creation du serializer ReservationSerializer
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ["id", "statut","salle","utilisateur","debut","fin","cree_le","motif"]
        read_only_fields = ["utilisateur"]
        # reservation dont fin n'est pas strictement postérieure a debut




# TODO : votre code ici
