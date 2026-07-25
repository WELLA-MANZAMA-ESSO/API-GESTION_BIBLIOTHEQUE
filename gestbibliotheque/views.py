from rest_framework.viewsets import ModelViewSet
from gestbibliotheque.serializers import AuteurListSerializer,LivreListSerializer,CategorieSerializer,AuteurDetailSerializer,LivreDetailSerializer
from gestbibliotheque.models import Auteur,Livre,Categorie
from utilisateurs.models import Utilisateur
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

    
