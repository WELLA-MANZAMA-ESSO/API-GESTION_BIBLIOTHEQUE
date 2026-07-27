from rest_framework.test import APITestCase
from gestbibliotheque.models import Auteur,Livre,Categorie
from utilisateurs.models import Utilisateur
from django.urls import reverse_lazy,reverse


# test CRUD du views

class APItestAuteur(APITestCase):

    def setUp(self):
        self. url=reverse_lazy('auteur-list')
        self.auteur=Auteur.objects.create(nom='Camus',prenom='Albert',age=45,pays='France')
        # créons un user et identifions le
        self.user=Utilisateur.objects.create_user(username='johny',email='johny01@gmail.com')
        self.client.force_authenticate(user=self.user)

    # create
    def test_list_auteur(self):
        response=self.client.get(self.url)
        self.assertEqual(response.status_code,200)
        resultat=[
            {
                'id':self.auteur.pk,
                'nom':self.auteur.nom,
                'prenom':self.auteur.prenom,
                
            }
        ]
        
        self.assertEqual(resultat,response.json())

        # test pour le detail
    def test_detail_auteur(self):
        url=reverse('auteur-detail',kwargs={'pk':self.auteur.pk})
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)
        resultat_attendu={
                'id':self.auteur.pk,
                'nom':self.auteur.nom,
                'prenom':self.auteur.prenom,
                'age':self.auteur.age,
                'pays':self.auteur.pays
            }
        
        self.assertEqual(resultat_attendu,response.json())


        # test de creation d'un auteur

    def test_create_auteur(self):
        
        response=self.client.post(self.url,data={'nom':'john','prenom':'ali','age':45,'pays':'Pays-bas'})
        self.assertEqual(response.status_code,403)
        # verifie qu'auccun auteur n'a été crée  
        self.assertEqual(Auteur.objects.count(),1)

    # test de mise à ajour 
    def test_update_auteur(self):
        
        url=reverse('auteur-detail',kwargs={'pk':self.auteur.pk})
        response=self.client.put(url,data={'nom':'jean','prenom':'ali','age':45,'pays':'France'})
        self.assertEqual(response.status_code,403)
        self.assertEqual(self.auteur.nom,'Camus')




        
        