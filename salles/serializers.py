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
        model = Reservations
        fields = ["id", "statut","salle","utilisateur","debut","fin","cree_le","motif"]
        read_only_fields = ["utilisateur"]
        # reservation dont fin n'est pas strictement postérieure a debut
        def validate(self, data):
            if data["fin"]<= data["debut"]:
                raise serializers.ValidationError("la date de debut ne doit pas etre plus recent que la fin")

            # une réservation qui chevauche une autre réservation CONFIRMEE de la même salle
            reservation=Reservation.objects.filter(salle=data["salle"],statut="Confirmee",
                                                    debut__ld=data["fin"],fin__gte=data["debut"])
            if self.instance:
                reservation=reservation.exclude(id=self.instance.id)
            if reservation.exists():
                raise serializers.ValidationError("Cette salle est deja reseree sur ce créneau")
            return data



# TODO : votre code ici
