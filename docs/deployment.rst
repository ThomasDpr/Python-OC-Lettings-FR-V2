Procédures de déploiement
==========================

Vue d'ensemble
--------------

Le projet utilise un pipeline CI/CD automatisé avec GitHub Actions pour déployer l'application sur Render.

Architecture du pipeline
------------------------

Le pipeline comprend 3 jobs séquentiels :

1. **Tests** : Linting + Tests unitaires + Couverture > 80%
2. **Docker** : Build et push de l'image vers Docker Hub
3. **Deploy** : Déploiement automatique sur Render

Workflow
--------

.. code-block:: text

   Push sur main
        ↓
   [Tests] flake8 + pytest
        ↓ (si succès)
   [Docker] build + push Docker Hub
        ↓ (si succès)
   [Deploy] webhook Render
        ↓
   Render pull l'image + redémarrage
        ↓
   Site mis à jour (≈2-3 min)

Configuration GitHub Actions
-----------------------------

Secrets GitHub requis
^^^^^^^^^^^^^^^^^^^^^

Dans **Settings > Secrets and variables > Actions**, configurer :

* ``DJANGO_SECRET_KEY`` : Clé secrète Django
* ``SENTRY_DSN`` : DSN Sentry pour monitoring
* ``DOCKERHUB_USERNAME`` : Nom d'utilisateur Docker Hub
* ``DOCKERHUB_TOKEN`` : Token d'accès Docker Hub
* ``RENDER_DEPLOY_HOOK_URL`` : URL webhook Render

Fichier .github/workflows/ci.yml
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le pipeline est défini dans ``.github/workflows/ci.yml``.

Déclenchement :

* Sur ``push`` sur branche ``main``
* Sur ``pull_request`` vers branche ``main``

**Note** : Seuls les push sur ``main`` déclenchent le build Docker et le déploiement.

Configuration Render
--------------------

Service configuré
^^^^^^^^^^^^^^^^^

* **Type** : Web Service
* **Image** : ``docker.io/thomasdpr/oc-lettings-prod:latest``
* **Port** : 8000
* **Auto-Deploy** : Désactivé (déploiement via CI uniquement)

Variables d'environnement
^^^^^^^^^^^^^^^^^^^^^^^^^^

Configurer dans Render Settings :

* ``SECRET_KEY`` : Clé secrète Django production
* ``DEBUG`` : ``False``
* ``ALLOWED_HOSTS`` : ``oc-lettings-prod-s43w.onrender.com``
* ``SENTRY_DSN`` : DSN Sentry

Lancer l'image Docker localement
---------------------------------

Commande unique pour pull + run
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   docker pull thomasdpr/oc-lettings-prod:latest && docker run -d -p 8000:8000 \
     --name oc-lettings \
     -e SECRET_KEY="votre-secret-key" \
     -e DEBUG="False" \
     -e ALLOWED_HOSTS="localhost,127.0.0.1" \
     thomasdpr/oc-lettings-prod:latest

Le site sera accessible sur http://localhost:8000

Arrêter le conteneur
^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   docker stop oc-lettings && docker rm oc-lettings

Processus de déploiement manuel
--------------------------------

1. Faire des modifications dans le code
2. Commit et push sur ``main`` :

.. code-block:: bash

   git add .
   git commit -m "feat: description des changements"
   git push origin main

3. Observer le pipeline dans l'onglet Actions de GitHub
4. Attendre 2-3 minutes
5. Vérifier le site : https://oc-lettings-prod-s43w.onrender.com

Gestion de Sentry
-----------------

Configuration
^^^^^^^^^^^^^

Sentry est configuré dans ``settings.py`` via la variable d'environnement ``SENTRY_DSN``.

Tester Sentry
^^^^^^^^^^^^^

Accéder à ``/sentry-debug/`` pour déclencher une erreur test.

L'erreur apparaîtra dans le dashboard Sentry > Issues.

Rollback en cas de problème
----------------------------

Si un déploiement pose problème :

1. Revenir au commit précédent :

.. code-block:: bash

   git revert HEAD
   git push origin main

2. Le pipeline se relance automatiquement
3. L'ancienne version est redéployée