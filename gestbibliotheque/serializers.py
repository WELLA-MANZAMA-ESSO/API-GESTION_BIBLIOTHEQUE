
from gestbibliotheque.models import Auteur,Categorie,Livre
from rest_framework.serializers import ModelSerializer


# serializers Auteur

class AuteurListSerializer(ModelSerializer):
    class Meta:
        model=Auteur
        fields=['id','nom','prenom']

class AuteurDetailSerializer(ModelSerializer):
    class Meta:
        model=Auteur
        fields=['id','nom','prenom','age','pays']


#Serializers Categorie

class CategorieSerializer(ModelSerializer):
    class Meta:
        model=Categorie
        fields=['id','nom']

class LivreListSerializer(ModelSerializer):
    class Meta:
        model=Livre
        fields=['id','titre']

class LivreDetailSerializer(ModelSerializer):
    class Meta:
        model=Livre
        fields=['id','titre','isbn','date_ajout','date_termine','emprunt','date_emprunt','date_retour','categorie','utilisateur','auteur']

