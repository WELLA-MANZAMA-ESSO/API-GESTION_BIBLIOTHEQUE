# 📚 API de Gestion de Bibliothèque

API REST développée avec **Django REST Framework** permettant de gérer une bibliothèque : livres, auteurs, catégories, emprunts, et utilisateurs avec gestion de rôles (lecteur, bibliothécaire, admin).

##  Fonctionnalités

- Gestion complète des livres, auteurs et catégories (CRUD)
- Système de rôles : **lecteur**, **bibliothécaire**, **administrateur**, avec permissions différenciées
- Sérialisation adaptée selon le contexte (liste allégée / détail complet avec relations imbriquées)
- Suivi de l'état des livres : emprunt, date d'emprunt, date de retour
- Tests unitaires couvrant les modèles, serializers et vues (avec mocks pour les appels externes)

##  Stack technique

- Python 3.11
- Django 5.2
- Django REST Framework
- PostgreSQL
- python-decouple (gestion des variables d'environnement)

## Installation

### Prérequis

- Python 3.11 ou supérieur
- PostgreSQL installé et en cours d'exécution
- pip

### Étapes

1. **Cloner le repository**
```bash
git clone https://github.com/WELLA-MANZAMA-ESSO/API-GESTION_BIBLIOTHEQUE.git
cd API-GESTION_BIBLIOTHEQUE
```

2. **Créer et activer un environnement virtuel**
```bash
python -m venv env
# Windows
env\Scripts\activate
# macOS/Linux
source env/bin/activate
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

4. **Configurer les variables d'environnement**

Copier le fichier d'exemple puis renseigner vos propres valeurs :
```bash
cp .env.example .env
```

Contenu attendu du `.env` :
```
SECRET_KEY=votre_cle_secrete_django
DEBUG=True

DB_NAME=bibliotheque
DB_USER=postgres
DB_PASSWORD=votre_mot_de_passe
DB_HOST=localhost
DB_PORT=5432
```

Pour générer une `SECRET_KEY` :
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

5. **Créer la base de données PostgreSQL**
```sql
CREATE DATABASE bibliotheque;
```

6. **Appliquer les migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

7. **Créer un compte administrateur**
```bash
python manage.py createsuperuser
```

8. **Lancer le serveur**
```bash
python manage.py runserver
```

L'API est accessible sur `http://127.0.0.1:8000/`

##  Authentification

 L'authentification par token JWT (endpoints `/token/` et `/token/refresh/`) n'est pas encore mise en place côté API. Actuellement, l'accès authentifié est vérifié dans les tests via `force_authenticate`.

##  Rôles et permissions

| Rôle | Consulter | Emprunter | Ajouter/Modifier | Supprimer | Gérer les utilisateurs |
|---|---|---|---|---|---|
| **Lecteur** | ✅ | ✅ | ❌ | ❌ | ❌ |
| **Bibliothécaire** | ✅ | ✅ | ✅ | ❌ | ❌ |
| **Admin** | ✅ | ✅ | ✅ | ✅ | ✅ |

##  Endpoints principaux

| Méthode | Endpoint | Description |
|---|---|---|
| GET | `/livre/` | Liste des livres |
| POST | `/livre/` | Ajouter un livre *(bibliothécaire/admin)* |
| GET | `/livre/{id}/` | Détail d'un livre (auteur, catégorie et propriétaire imbriqués) |
| PUT/PATCH | `/livre/{id}/` | Modifier un livre *(bibliothécaire/admin)* |
| DELETE | `/livre/{id}/` | Supprimer un livre *(admin)* |
| GET | `/auteur/` | Liste des auteurs |
| POST | `/auteur/` | Ajouter un auteur *(bibliothécaire/admin)* |
| GET | `/categorie/` | Liste des catégories |
| GET | `/utilisateur/` | Liste des utilisateurs |

##  Tests

Lancer l'ensemble des tests :
```bash
python manage.py test
```

Les tests couvrent :
- La logique métier des modèles (statuts, méthodes personnalisées)
- La validation des serializers
- Les permissions par rôle sur chaque action (lecture, création, modification, suppression)
- Le comportement des vues via `APITestCase`

## 📁 Structure du projet

```
API-GESTION_BIBLIOTHEQUE/
├── manage.py
├── requirements.txt
├── .env.example
├── bibliotheque/            # Configuration principale Django
│   ├── settings.py
│   └── urls.py
├── utilisateurs/            # Gestion des comptes et des rôles
│   ├── models.py
│   ├── serializers.py
│   ├── permissions.py
│   ├── views.py
│   └── tests.py
└── gestbibliotheque/        # Cœur métier : livres, auteurs, catégories
    ├── models.py
    ├── serializers.py
    ├── mixins.py
    ├── permissions.py
    ├── views.py
    ├── urls.py
    └── tests.py
```

## Auteur

Développé par **Wella Manzama-Esso**, étudiant en Licence 2 Génie Logiciel, dans le cadre de l'apprentissage de Django REST Framework.