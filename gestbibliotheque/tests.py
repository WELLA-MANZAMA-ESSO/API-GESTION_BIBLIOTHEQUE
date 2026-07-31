from rest_framework.test import APITestCase
from gestbibliotheque.models import Auteur,Livre,Categorie
from utilisateurs.models import Utilisateur
from django.urls import reverse_lazy,reverse


# test CRUD du views

class APItestAuteur(APITestCase):

    def setUp(self):
        self.url=reverse_lazy('auteur-list')
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

    # test de suppression

    def test_delete_auteur(self):
        url=reverse('auteur-detail',kwargs={'pk':self.auteur.pk})
        response=self.client.delete(url)
        self.assertEqual(response.status_code,403)
        self.assertTrue(Auteur.objects.exists())


# test CRUD pou le livre

class APITestLivre(APITestCase):
    maxDiff=None
    def setUp(self):
        
        self.user=Utilisateur.objects.create_user(username='johny',email='johny01@gmail.com')
        self.client.force_authenticate(user=self.user)
        self.auteur=Auteur.objects.create(nom='Camus',prenom='Albert',age=45,pays='France')
        self.categorie=Categorie.objects.create(nom='Drame')
        self.livre=Livre.objects.create(titre='Mon père mon Héro',isbn='0537846',categorie=self.categorie,auteur=self.auteur,utilisateur=self.user)
        

        self.url=reverse_lazy('livre-list')
        self.detail_url=reverse('livre-detail',kwargs={'pk':self.livre.pk})

    # test list
    def test_list_livre(self):
        response=self.client.get(self.url)
        self.assertEqual(response.status_code,200)
        resultat_attendu=[
            {
                'id':self.livre.pk,
                'titre':self.livre.titre,
                'isbn':self.livre.isbn,
                'date_retour':self.livre.date_retour,
                'date_ajout':self.livre.date_ajout.isoformat().replace('+00:00', 'Z'),
                'date_termine':self.livre.date_termine,
                'emprunt':self.livre.emprunt,
                'date_emprunt':self.livre.date_emprunt,
                'categorie':str(self.categorie),
                'auteur':str(self.auteur),
                'utilisateur':str(self.user),
                
            }
        ]

        self.assertEqual(resultat_attendu,response.json())

    # test detail 
    def test_detail_livre(self):
        response=self.client.get(self.detail_url)
        self.assertEqual(response.status_code,200)
        resultat_attendu ={

                'id':self.livre.pk,
                'titre':self.livre.titre,
                'isbn':self.livre.isbn,
                'date_retour':self.livre.date_retour,
                'date_ajout':self.livre.date_ajout.isoformat().replace('+00:00', 'Z'),
                'date_termine':self.livre.date_termine,
                'emprunt':self.livre.emprunt,
                'date_emprunt':self.livre.date_emprunt,
                'categorie':{
                    'id':self.categorie.pk,
                    'nom':self.categorie.nom

                },
                'auteur':{
                    'id':self.auteur.pk,
                    'nom':self.auteur.nom,
                    'prenom':self.auteur.prenom,
                    'age':self.auteur.age,
                    'pays':self.auteur.pays
                },
                'utilisateur':{
                    'id':self.user.pk,
                    'username':self.user.username,
                    'email':self.user.email,
                    'telephone':self.user.telephone,
                    'role':self.user.role
                }
                
                
        }

        self.assertEqual(resultat_attendu,response.json())

    # test create livre
    def test_create_livre(self):
        response=self.client.post(self.url,data={'titre':'Jean piègé'})
        self.assertEqual(response.status_code,403)
        self.assertTrue(Livre.objects.count(),1)

    # test update livre

    def test_update_livre(self):
        response=self.client.put(self.detail_url,data={'titre':'les larmes d\'une bonne' })
        self.assertEqual(response.status_code,403)
        self.assertEqual(self.livre.titre,'Mon père mon Héro')

    # test delete livre

    def test_delete_livre(self):
        response=self.client.delete(self.detail_url)
        self.assertEqual(response.status_code,403)
        self.assertTrue(Livre.objects.exists())







        
        