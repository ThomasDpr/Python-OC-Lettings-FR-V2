# 🏠 Orange County Lettings

Site web de gestion de locations immobilières pour Orange County Lettings, une start-up en pleine expansion aux États-Unis.

[![CI Status](https://github.com/ThomasDpr/Python-OC-Lettings-FR-V2/actions/workflows/ci.yml/badge.svg)](https://github.com/ThomasDpr/Python-OC-Lettings-FR-V2/actions)
[![Documentation Status](https://readthedocs.org/projects/python-oc-lettings-fr-v2/badge/?version=latest)](https://python-oc-lettings-fr-v2.readthedocs.io/)
[![Python Version](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)
[![Django Version](https://img.shields.io/badge/django-3.0-green.svg)](https://www.djangoproject.com/)

---

## 📋 Table des matières

- [Description du projet](#-description-du-projet)
- [Architecture](#-architecture)
- [Technologies](#-technologies)
- [Installation locale](#-installation-locale)
- [Tests et qualité](#-tests-et-qualité)
- [Documentation](#-documentation)
- [Docker](#-docker)
- [Déploiement](#-déploiement)
- [Monitoring avec Sentry](#-monitoring-avec-sentry)

---

## 📝 Description du projet

Ce projet est une refonte complète de l'application OC Lettings, passant d'une architecture monolithique à une architecture modulaire. Les principales améliorations incluent :

- ✅ **Refactorisation modulaire** : Séparation en 3 applications Django distinctes
- ✅ **Pipeline CI/CD** : Automatisation complète du déploiement via GitHub Actions
- ✅ **Containerisation** : Application Dockerisée et disponible sur Docker Hub
- ✅ **Monitoring** : Intégration de Sentry pour le suivi des erreurs
- ✅ **Documentation** : Documentation technique complète sur Read the Docs
- ✅ **Tests** : Couverture de tests > 80% (actuellement 99%)
- ✅ **Qualité** : Linting avec flake8, respect strict de PEP8

**Liens rapides** :
- 🌐 **Site en production** : [https://oc-lettings-prod-s43w.onrender.com](https://oc-lettings-prod-s43w.onrender.com)
- 📚 **Documentation** : [https://python-oc-lettings-fr-v2.readthedocs.io](https://python-oc-lettings-fr-v2.readthedocs.io)
- 🐳 **Docker Hub** : [https://hub.docker.com/r/thomasdpr/oc-lettings-prod](https://hub.docker.com/r/thomasdpr/oc-lettings-prod)

---

## 🏗️ Architecture

L'application est structurée en **3 applications Django** :

### 1. `oc_lettings_site` (Application principale)
- Configuration du projet Django
- Page d'accueil
- Gestion des erreurs personnalisées (404, 500)
- Intégration Sentry

### 2. `lettings` (Gestion des locations)
- Modèle `Address` : Gestion des adresses des propriétés
- Modèle `Letting` : Gestion des locations disponibles
- Vues et templates pour la liste et le détail des locations
- Namespace d'URL : `lettings:`

### 3. `profiles` (Gestion des profils utilisateurs)
- Modèle `Profile` : Extension du modèle User Django
- Vues et templates pour la liste et le détail des profils
- Namespace d'URL : `profiles:`

**Schéma relationnel** :
```
User (Django) ←→ Profile (one-to-one)
Address ←→ Letting (one-to-one)
```

---

## 🛠️ Technologies

### Backend
- **Python 3.11**
- **Django 3.0** - Framework web
- **Gunicorn** - Serveur WSGI pour production

### Base de données
- **SQLite3** - Base de données (développement et production)

### Tests et qualité
- **pytest** - Framework de tests
- **pytest-django** - Plugin pytest pour Django
- **pytest-cov** - Mesure de la couverture de tests
- **flake8** - Linting Python (respect PEP8)

### Monitoring
- **Sentry** - Surveillance des erreurs et logging

### Déploiement
- **Docker** - Containerisation de l'application
- **Docker Hub** - Registre d'images Docker
- **GitHub Actions** - CI/CD
- **Render** - Hébergement en production
- **WhiteNoise** - Gestion des fichiers statiques

### Documentation
- **Sphinx** - Générateur de documentation
- **Read the Docs** - Hébergement de la documentation

---

## 💻 Installation locale

### Prérequis

- Python 3.11 ou supérieur
- Git
- SQLite3 (inclus avec Python)

### Étapes d'installation

#### 1. Cloner le repository

```bash
git clone https://github.com/ThomasDpr/Python-OC-Lettings-FR-V2.git
cd Python-OC-Lettings-FR-V2
```

#### 2. Créer et activer l'environnement virtuel

**macOS / Linux** :
```bash
python -m venv venv
source venv/bin/activate
```

**Windows** :
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

#### 3. Installer les dépendances

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

#### 4. Configuration

Créer un fichier `.env` à la racine du projet :

```bash
SECRET_KEY=votre-cle-secrete-developpement
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
SENTRY_DSN=  # Optionnel pour le développement local
```

#### 5. Migrations de base de données

```bash
python manage.py migrate
```

#### 6. Créer un superutilisateur (optionnel)

```bash
python manage.py createsuperuser
```

Ou utiliser le compte de test existant :
- **Utilisateur** : `admin`
- **Mot de passe** : `Abc1234!`

#### 7. Lancer le serveur de développement

```bash
python manage.py runserver
```

L'application est accessible sur **http://localhost:8000**

**Interface d'administration** : http://localhost:8000/admin

---

## 🧪 Tests et qualité

### Lancer les tests

```bash
pytest
```

### Vérifier la couverture de tests

```bash
pytest --cov=. --cov-report=term-missing
```

**Couverture actuelle** : 99.16% ✅ (objectif : > 80%)

### Rapport de couverture HTML

```bash
pytest --cov=. --cov-report=html
open htmlcov/index.html
```

### Linter le code

```bash
flake8
```

Le projet respecte strictement les normes **PEP8** avec une longueur de ligne maximale de 99 caractères.

### Organisation des tests

Les tests sont organisés par application :

```
lettings/tests/
├── test_models.py      # Tests des modèles Address et Letting
├── test_views.py       # Tests des vues (index, detail, 404)
└── test_urls.py        # Tests des URLs et routing

profiles/tests/
├── test_models.py      # Tests du modèle Profile
├── test_views.py       # Tests des vues
└── test_urls.py        # Tests des URLs

oc_lettings_site/tests/
├── test_views.py       # Tests de la page d'accueil
├── test_errors.py      # Tests des pages 404 et 500
└── test_urls.py        # Tests des URLs
```

---

## 📚 Documentation

### Documentation complète

La documentation technique du projet est disponible sur Read the Docs :

**📖 [Accéder à la documentation](https://python-oc-lettings-fr-v2.readthedocs.io/)**

La documentation contient :
- Description détaillée du projet et contexte
- Instructions d'installation complètes
- Guide de démarrage rapide
- Technologies et langages utilisés
- Structure de la base de données et modèles
- Interfaces de programmation (URLs, vues)
- Guide d'utilisation avec cas d'usage
- Procédures de déploiement et gestion

### Générer la documentation localement

```bash
cd docs
make html
```

La documentation sera générée dans `docs/_build/html/index.html`.

**Note** : La documentation est automatiquement mise à jour sur Read the Docs à chaque push sur la branche `main`.

---

## 🐳 Docker

### Utiliser l'image Docker pré-construite

L'image Docker de l'application est disponible sur Docker Hub et est la même que celle utilisée en production.

**Prérequis** : Docker installé ([Télécharger Docker](https://www.docker.com/get-started))

### Commande unique pour récupérer et lancer l'application

```bash
docker pull thomasdpr/oc-lettings-prod:latest && docker run -d -p 8000:8000 --name oc-lettings -e SECRET_KEY="dev-secret-key" -e DEBUG="False" -e ALLOWED_HOSTS="localhost,127.0.0.1" thomasdpr/oc-lettings-prod:latest
```

**Explication de la commande** :
- `docker pull` : Télécharge l'image depuis Docker Hub
- `&&` : Exécute la commande suivante seulement si la première réussit
- `docker run` : Crée et démarre un conteneur
- `-d` : Mode détaché (arrière-plan)
- `-p 8000:8000` : Expose le port 8000 (accès via http://localhost:8000)
- `--name oc-lettings` : Nom du conteneur pour faciliter la gestion
- `-e` : Variables d'environnement nécessaires à l'application

**Le site sera accessible sur http://localhost:8000**

### Commandes utiles

**Voir les logs du conteneur** :
```bash
docker logs -f oc-lettings
```

**Arrêter le conteneur** :
```bash
docker stop oc-lettings
```

**Redémarrer le conteneur** :
```bash
docker start oc-lettings
```

**Arrêter et supprimer le conteneur** :
```bash
docker stop oc-lettings && docker rm oc-lettings
```

**Voir l'état du conteneur** :
```bash
docker ps -a
```

### Construire l'image localement (optionnel)

Si vous souhaitez construire l'image Docker vous-même :

```bash
docker build -t oc-lettings-local .
docker run -d -p 8000:8000 --name oc-lettings-local -e SECRET_KEY="dev-key" -e DEBUG="False" -e ALLOWED_HOSTS="localhost,127.0.0.1" oc-lettings-local
```

---

## 🚀 Déploiement

### Pipeline CI/CD

Le projet utilise **GitHub Actions** pour automatiser le déploiement. Le pipeline comprend 3 jobs séquentiels :

```
Push sur main
    ↓
[Job 1: Tests]
- Linting avec flake8
- Tests unitaires et intégration avec pytest
- Vérification couverture > 80%
    ↓ (si succès)
[Job 2: Docker]
- Build de l'image Docker
- Push vers Docker Hub avec 2 tags :
  - thomasdpr/oc-lettings-prod:latest
  - thomasdpr/oc-lettings-prod:<commit-sha>
    ↓ (si succès)
[Job 3: Deploy]
- Appel du webhook Render
- Render pull l'image depuis Docker Hub
- Redémarrage du service
    ↓
Site mis à jour en production (≈2-3 min)
```

**Fichier de configuration** : `.github/workflows/ci.yml`

### Configuration des secrets GitHub

Dans **Settings > Secrets and variables > Actions**, les secrets suivants doivent être configurés :

| Secret | Description |
|--------|-------------|
| `DJANGO_SECRET_KEY` | Clé secrète Django pour production |
| `SENTRY_DSN` | DSN Sentry pour le monitoring des erreurs |
| `DOCKERHUB_USERNAME` | Nom d'utilisateur Docker Hub |
| `DOCKERHUB_TOKEN` | Token d'accès Docker Hub |
| `RENDER_DEPLOY_HOOK_URL` | URL du webhook Render pour déclenchement déploiement |

### Déclenchement du pipeline

**Branches** :
- **`main`** : Déclenche tests + build Docker + déploiement
- **Autres branches** : Déclenche uniquement les tests

**Pull Requests** : Tests uniquement (pas de déploiement)

### Processus de déploiement

1. Faire des modifications dans le code
2. Commit et push sur `main` :
   ```bash
   git add .
   git commit -m "feat: description des changements"
   git push origin main
   ```
3. Observer le pipeline dans l'onglet **Actions** de GitHub
4. Attendre 2-3 minutes
5. Vérifier le site : [https://oc-lettings-prod-s43w.onrender.com](https://oc-lettings-prod-s43w.onrender.com)

### Configuration Render

Le service Render est configuré pour :
- **Type** : Web Service
- **Image Docker** : `docker.io/thomasdpr/oc-lettings-prod:latest`
- **Port** : 8000
- **Auto-Deploy** : ❌ Désactivé (déploiement via CI uniquement)

**Variables d'environnement Render** :
- `SECRET_KEY` : Clé secrète Django (production)
- `DEBUG` : `False`
- `ALLOWED_HOSTS` : `oc-lettings-prod-s43w.onrender.com`
- `SENTRY_DSN` : DSN Sentry

### Rollback en cas de problème

Si un déploiement pose problème :

```bash
# Revenir au commit précédent
git revert HEAD
git push origin main

# Le pipeline se relance automatiquement
# L'ancienne version est redéployée
```

---

## 🔍 Monitoring avec Sentry

### Configuration

Sentry est intégré pour surveiller les erreurs et les logs en production.

**Configuration** : `oc_lettings_site/settings.py` (lignes 140-156)

La variable d'environnement `SENTRY_DSN` doit être configurée pour activer Sentry.

### Tester Sentry

**En local** :
```bash
# Démarrer le serveur
python manage.py runserver

# Déclencher une erreur de test
curl http://localhost:8000/sentry-debug/
```

**En production** :
```bash
curl https://oc-lettings-prod-s43w.onrender.com/sentry-debug/
```

L'erreur apparaîtra dans le dashboard Sentry > Issues.

### Points de logging

Des logs sont insérés aux points stratégiques :
- Erreurs 404 sur les vues `letting` et `profile`
- Exceptions non gérées (capturées automatiquement par Sentry)
- Erreurs serveur 500

**Exemple de log** :
```python
logger.error(
    "Letting not found",
    extra={"letting_id": letting_id}
)
```

---

## 📦 Structure du projet

```
Python-OC-Lettings-FR-V2/
├── .github/
│   └── workflows/
│       └── ci.yml                  # Pipeline CI/CD GitHub Actions
├── docs/                            # Documentation Sphinx
│   ├── conf.py                      # Configuration Sphinx
│   ├── index.rst                    # Page d'accueil documentation
│   ├── project_overview.rst         # Description projet
│   ├── installation.rst             # Instructions installation
│   ├── quickstart.rst               # Démarrage rapide
│   ├── technologies.rst             # Technologies utilisées
│   ├── database_models.rst          # Modèles de données
│   ├── api_reference.rst            # APIs internes
│   ├── usage_guide.rst              # Guide d'utilisation
│   └── deployment.rst               # Procédures déploiement
├── lettings/                        # App Django - Gestion locations
│   ├── migrations/                  # Migrations Django
│   ├── tests/                       # Tests unitaires
│   ├── models.py                    # Modèles Address, Letting
│   ├── views.py                     # Vues
│   ├── urls.py                      # Configuration URLs
│   └── admin.py                     # Configuration admin
├── profiles/                        # App Django - Gestion profils
│   ├── migrations/                  # Migrations Django
│   ├── tests/                       # Tests unitaires
│   ├── models.py                    # Modèle Profile
│   ├── views.py                     # Vues
│   ├── urls.py                      # Configuration URLs
│   └── admin.py                     # Configuration admin
├── oc_lettings_site/                # App Django principale
│   ├── migrations/                  # Migrations Django
│   ├── tests/                       # Tests unitaires
│   ├── settings.py                  # Configuration Django
│   ├── urls.py                      # URLs principales
│   ├── views.py                     # Vues (home, erreurs)
│   ├── wsgi.py                      # Configuration WSGI
│   └── asgi.py                      # Configuration ASGI
├── static/                          # Fichiers statiques
│   ├── css/
│   ├── js/
│   └── assets/
├── templates/                       # Templates Django
│   ├── base.html                    # Template de base
│   ├── 404.html                     # Page erreur 404
│   ├── 500.html                     # Page erreur 500
│   ├── lettings/                    # Templates lettings
│   ├── profiles/                    # Templates profiles
│   └── oc_lettings_site/            # Templates home
├── .dockerignore                    # Fichiers exclus du build Docker
├── .gitignore                       # Fichiers exclus de Git
├── .readthedocs.yaml                # Configuration Read the Docs
├── Dockerfile                       # Instructions build Docker
├── manage.py                        # Script Django
├── oc-lettings-site.sqlite3         # Base de données SQLite
├── requirements.txt                 # Dépendances Python
├── setup.cfg                        # Configuration pytest/flake8
└── README.md                        # Ce fichier
```

---

## 🤝 Contribuer

### Workflow de contribution

1. Fork le projet
2. Créer une branche (`git checkout -b feature/AmazingFeature`)
3. Commit les changements (`git commit -m 'feat: add amazing feature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

### Standards de code

- Respecter **PEP8** (vérifier avec `flake8`)
- Ajouter des **tests** pour toute nouvelle fonctionnalité
- Maintenir la **couverture > 80%**
- Ajouter des **docstrings** sur les nouvelles fonctions/classes
- Utiliser des **messages de commit clairs** (Conventional Commits)

---

## 📄 Licence

Ce projet est un projet éducatif réalisé dans le cadre de la formation OpenClassrooms.

---

## 👤 Auteur

**Thomas Dupré**

- GitHub: [@ThomasDpr](https://github.com/ThomasDpr)
- Projet: [Python-OC-Lettings-FR-V2](https://github.com/ThomasDpr/Python-OC-Lettings-FR-V2)

---

## 📞 Support

Pour toute question ou problème :
- Consulter la [documentation](https://python-oc-lettings-fr-v2.readthedocs.io/)
- Ouvrir une [issue](https://github.com/ThomasDpr/Python-OC-Lettings-FR-V2/issues)
- Vérifier les [logs Sentry](https://sentry.io) en cas d'erreur en production

---

**Dernière mise à jour** : Janvier 2026
