from rest_framework.viewsets import ModelViewSet
from utilisateurs.models import Utilisateur
from utilisateurs.serializers import UtilisateurDetailSerializer,UtilisateurListSerializer
from rest_framework.permissions import IsAuthenticated
from utilisateurs.permissions import IsAdmin,IsBibliothecaireOAdmin

# class mixins

class MultipleSerializerMixin:
    detail_serializer_class=None
    def get_serializer_class(self):
        if self.action=='retrieve' and  self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class() 


#  views utilisateur 

class UtilisateurView(MultipleSerializerMixin,ModelViewSet):
    serializer_class=UtilisateurListSerializer
    detail_serializer_class=UtilisateurDetailSerializer

    def get_queryset(self):
        utilisateur=Utilisateur.objects.all()
        return utilisateur

    # fonction pour gérer les permissiosns
    def get_permissions(self):
        if self.action in ['create','update','update_partial']:
            return [IsBibliothecaireOAdmin()]
        if self.action =='destroy':
            return [IsAdmin()]
        return [IsAuthenticated()]

