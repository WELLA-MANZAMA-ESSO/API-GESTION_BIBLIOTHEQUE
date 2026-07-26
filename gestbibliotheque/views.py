from rest_framework.viewsets import ModelViewSet
from gestbibliotheque.serializers import AuteurListSerializer,LivreListSerializer,CategorieSerializer,AuteurDetailSerializer,LivreDetailSerializer
from gestbibliotheque.models import Auteur,Livre,Categorie

# views Mixins

class MultipleSerializerMixin:
    detail_serializer_class = None
    def get_serializer_class(self):
        if self.action=='retreive' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()

# views Auteur 

class AuteurView(MultipleSerializerMixin,ModelViewSet):
    serializer_class=AuteurListSerializer
    detail_serializer_class=AuteurDetailSerializer



    def get_queryset(self):
        auteur=Auteur.objects.all()
        return auteur


# views Categorie

class CategorieView(ModelViewSet):

    serializer_class=CategorieSerializer

    def get_queryset(self):
        categorie=Categorie.objects.all()
        return categorie

# views Livre

class LivreView(MultipleSerializerMixin,ModelViewSet):
    serializer_class=LivreListSerializer
    detail_serializer_class=LivreDetailSerializer

    def get_queryset(self):
        livre=Livre.objects.all()
        return livre
    
