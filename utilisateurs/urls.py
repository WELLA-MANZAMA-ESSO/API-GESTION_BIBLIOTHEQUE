from django.urls import path,include
from rest_framework import routers
from utilisateurs.views import UtilisateurView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

router=routers.SimpleRouter()
router.register('utilisateur',UtilisateurView,basename='utilisateur')


urlpatterns = [
    path('token/obtain/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('token/refresh/',TokenRefreshView.as_view(),name='token_refresh_pair'),
    path('',include(router.urls)),

]