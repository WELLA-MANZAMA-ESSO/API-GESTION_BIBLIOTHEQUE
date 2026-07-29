from rest_framework.serializers import ModelSerializer
from utilisateurs.models import Utilisateur

# serializers utilisateur

class UtilisateurListSerializer(ModelSerializer):
    class Meta:
        model=Utilisateur
        fields=['id','username','email']
        
class UtilisateurDetailSerializer(ModelSerializer):
    class Meta:
        model=Utilisateur
        fields=['id','username','email','telephone','role']
        read_only_fields=['role']