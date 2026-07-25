from django.db import models
from utilisateurs.models import Utilisateur

# models Auteur-Categorie-Livre

class Auteur(models.Model):
    nom=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    age=models.PositiveIntegerField(verbose_name="Entrer votre âge")
    pays=models.CharField(max_length=50)

    def __str__(self):
        return self.nom

    



# 

class Categorie(models.Model):
    nom=models.CharField(max_length=50)

    def __str__(self):
        return self.nom


# 

class Livre(models.Model):
    titre=models.CharField(max_length=50)
    isbn=models.CharField(max_length=10,unique=True, null=True)
    date_ajout=models.DateTimeField(auto_created=True)
    date_termine=models.DateTimeField(blank=True, null=True)
    emprunt=models.BooleanField(default=False)
    date_emprunt=models.DateTimeField(blank=True,null=True)
    date_retour=models.DateTimeField(blank=True,null=True)

    auteur=models.ForeignKey(Auteur, on_delete=models.CASCADE, related_name='auteur')
    livre=models.ForeignKey(Categorie,on_delete=models.CASCADE,related_name='categorie')
    utilisateur=models.ForeignKey(Utilisateur,on_delete=models.CASCADE,related_name='utilisateur')