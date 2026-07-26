
from gestbibliotheque.models import Auteur,Categorie,Livre
from rest_framework.serializers import ModelSerializer,StringRelatedField,PrimaryKeyRelatedField
from rest_framework import serializers
from utilisateurs.serializers import UtilisateurDetailSerializer


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
    # permettons l'affichage d'un livre avec son auteur et sa categoie
    auteur=serializers.StringRelatedField(read_only=True)
    categorie=serializers.StringRelatedField(read_only=True)
    utilisateur=serializers.StringRelatedField(read_only=True)

    class Meta:
        model=Livre
        fields=['id','titre','isbn','date_ajout','date_termine','emprunt','date_emprunt','date_retour','categorie','utilisateur','auteur']

class LivreDetailSerializer(ModelSerializer):
    auteur=AuteurDetailSerializer(read_only=True)
    utilisateur=UtilisateurDetailSerializer(read_only=True)
    categorie=CategorieSerializer(read_only=True)
    auteur_id=PrimaryKeyRelatedField(
        queryset=Auteur.objects.all() ,source='auteur', write_only=True
    )

    categorie_id=serializers.PrimaryKeyRelatedField(
        queryset=Categorie.objects.all(), source='categorie',write_only=True
    )
    class Meta:
        model=Livre
        fields=['id','titre','isbn','date_ajout','date_termine','emprunt','date_emprunt','date_retour','categorie','utilisateur','auteur','auteur_id','categorie_id']
        read_only_fields=['utilisateur']

