from django.db import models
from django.contrib.auth.models import AbstractUser

# models

class Utilisateur(AbstractUser):
    ROLE_CHOICE=[
        ('lecteur','lecteur'),
        ('bibliothecaire','bibliothecaire'),
        ('admin','admin'),
    ]
    telephone=models.CharField(max_length=60,blank=True)
    role=models.CharField(max_length=50,choices=ROLE_CHOICE,default='lecteur')

    def __str__(self):
        return self.username

    
