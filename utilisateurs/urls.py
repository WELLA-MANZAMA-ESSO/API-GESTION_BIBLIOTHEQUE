from django.urls import path,include
from rest_framework import routers
from utilisateurs.views import UtilisateurView

router=routers.SimpleRouter()
router.register('utilisateur',UtilisateurView,basename='utilisateur')


urlpatterns = [
    path('',include(router.urls)),

]