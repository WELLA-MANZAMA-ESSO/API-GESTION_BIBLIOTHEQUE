from django.urls import path,include
from rest_framework import routers

from gestbibliotheque.views import AuteurView,LivreView,CategorieView

router=routers.SimpleRouter()
router.register('auteur',AuteurView,basename='auteur')
router.register('livre',LivreView,basename='livre')
router.register('categorie',CategorieView,basename='categorie')

urlpatterns = [
    path('',include(router.urls)),

]