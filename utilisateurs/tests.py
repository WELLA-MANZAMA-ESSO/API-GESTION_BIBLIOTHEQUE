from rest_framework.test import APITestCase
from utilisateurs.models import Utilisateur
from django.urls import reverse,reverse_lazy

# test CRUD d'utilisateur


class ApitestUtilisateur(APITestCase):

    def setUp(self):
        self.user=Utilisateur.objects.create_user(username='Ali',email='alibonko9@gmail.com')
        self.client.force_authenticate(user=self.user)

        self.url=reverse_lazy('utilisateur-list')
        self.detail_url=reverse('utilisateur-detail',kwargs={'pk':self.user.pk})

    # test list 

    def test_list_user(self):
        response=self.client.get(self.url)
        self.assertEqual(response.status_code,200)
        resultat_attendu=[
            {
            'id':self.user.pk,
            'username':self.user.username,
            'email':self.user.email
        }
        ]

        self.assertEqual(resultat_attendu,response.json())
    # test detail user

    def test_detail_user(self):
        response=self.client.get(self.detail_url)
        self.assertEqual(response.status_code,200)

        resultat_attendu={
                    'id':self.user.pk,
                    'username':self.user.username,
                    'email':self.user.email,
                    'telephone':self.user.telephone,
                    'role':self.user.role
                }

        self.assertEqual(resultat_attendu,response.json())

    # test create user
    def test_create_user(self):
        response=self.client.post(self.detail_url,data={'username':'Eric','email':'ericjojo@gmail.com'})
        self.assertEqual(response.status_code,405)
        # verifions que la création à été refusée avec succès 
        self.assertEqual(Utilisateur.objects.count(),1)

    # test update user

    def test_update_user(self):
        response=self.client.put(self.detail_url,data={'username':'Lola','email':'alibonko9@gmail.com'})
        self.assertEqual(response.status_code,403)
        self.assertEqual(self.user.username,'Ali')

    #test delete user

    def test_delete_user(self):
        response=self.client.delete(self.detail_url)
        self.assertEqual(response.status_code,403)
        self.assertTrue(Utilisateur.objects.exists())

                
        



    


