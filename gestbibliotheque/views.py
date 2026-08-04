from rest_framework.viewsets import ModelViewSet
from gestbibliotheque.serializers import AuteurListSerializer,LivreListSerializer,CategorieSerializer,AuteurDetailSerializer,LivreDetailSerializer
from gestbibliotheque.models import Auteur,Livre,Categorie
from gestbibliotheque.permissions import IsAdmin,IsBibliothecaireOuAdmin
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

# views Mixins

class MultipleSerializerMixin:
    detail_serializer_class = None
    def get_serializer_class(self):
        if self.action=='retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()

# views Auteur 

class AuteurView(MultipleSerializerMixin,ModelViewSet):
    serializer_class=AuteurListSerializer
    detail_serializer_class=AuteurDetailSerializer




    def get_queryset(self):
        auteur=Auteur.objects.all()
        return auteur

    # fonction pour la permisson

    def get_permissions(self):
        if self.action in ['create','update','update_partials']:
            return [IsBibliothecaireOuAdmin()]
        if self.action == 'destroy':
            return [IsAdmin()]
        return [IsAuthenticated()]


# views Categorie

class CategorieView(ModelViewSet):

    serializer_class=CategorieSerializer

    def get_queryset(self):
        categorie=Categorie.objects.all()
        return categorie


    def get_permissions(self):
            if self.action in ['create','update','update_partials']:
                return [IsBibliothecaireOuAdmin()]
            if self.action == 'destroy':
                return [IsAdmin()]
            return [IsAuthenticated()]

# views Livre

class LivreView(MultipleSerializerMixin,ModelViewSet):
    serializer_class=LivreListSerializer
    detail_serializer_class=LivreDetailSerializer

    def get_queryset(self):
        livre=Livre.objects.all()
        return livre


    def get_permissions(self):
            if self.action in ['create','update','update_partials']:
                return [IsBibliothecaireOuAdmin()]
            if self.action == 'destroy':
                return [IsAdmin()]
            return [IsAuthenticated()]

    # Definissons la methode suivante pour permettre l'ajout automatique de l'utilisateur

    def perform_create(self, serializer):
        return serializer.save(utilisateur=self.request.user)

    # Actions 
    @action(detail=True,methods=['post'])
    def emprunter(self,request,pk):
        livre=self.get_object()
        livre.emprunter()
        return Response()

    @action(detail=True,methods=['post'])
    def rendre(self,request,pk):
        livre=self.get_object()
        livre.rendre()
        return Response()

    @action(detail=True,methods=['post'])
    def marquer_lu(self,request,pk):
        livre=self.get_object()
        livre.marquer_lu()
        return Response()        

    
    
