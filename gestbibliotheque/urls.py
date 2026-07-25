from django.urls import path,include
from rest_framework import routers

from gestbibliotheque.views import AuteurView

router=routers.SimpleRouter()
router.register('auteur',AuteurView,basename='auteur')

urlpatterns = [
    path('',include(router.urls)),

]