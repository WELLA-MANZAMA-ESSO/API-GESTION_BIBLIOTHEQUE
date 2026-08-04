from django.db import models, transaction
from utilisateurs.models import Utilisateur
from django.utils import timezone

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
    date_ajout=models.DateTimeField(auto_now_add=True)
    date_termine=models.DateTimeField(blank=True, null=True)
    emprunt=models.BooleanField(default=False)
    date_emprunt=models.DateTimeField(blank=True,null=True)
    date_retour=models.DateTimeField(blank=True,null=True)

    auteur=models.ForeignKey(Auteur, on_delete=models.CASCADE, related_name='auteur')
    categorie=models.ForeignKey(Categorie,on_delete=models.CASCADE,related_name='categorie')
    utilisateur=models.ForeignKey(Utilisateur,on_delete=models.CASCADE,related_name='utilisateur')


    def __str__(self):
        return self.titre

     # Mise en place des actions
    # Action emprunter
    transaction.atomic
    def emprunter(self):
        if self.emprunt:
            return
        self.emprunt=True
        self.date_ajout=timezone.now()
        self.date_retour=None
        self.save()
    # Action rendre le livre
    transaction.atomic
    def rendre(self):
        if self.emprunt:
            return
        self.emprunt=False
        self.date_retour=timezone.now()
        self.save()

    # Action  marquer comme lu
    transaction.atomic
    def marquer_lu(self):
        if self.date_retour is not None:
            return
        self.date_retour=timezone.now()
        self.save()

            