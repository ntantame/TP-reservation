"""Tache 4 : permissions personnalisees.

A FAIRE :
  - IsOwnerOrReadOnly : lecture pour tous, modification/suppression
    reservee a l'auteur de la reservation (obj.utilisateur).
"""
from rest_framework import permissions  # noqa: F401  (a utiliser)

# creation de IsOwnerOrReadOnly
class IsOwnerOrReadOnly(permissions.BasePermission):
    # lecture autorise par tout le monde
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
    # ecriture reserve a l'auteur
        return obj.user == request.user
# ppur la salle
class IsStaffOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff
# TODO : votre code ici
