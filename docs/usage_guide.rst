Guide d'utilisation
===================

Cas d'usage 1 : Consulter les locations
----------------------------------------

1. Accéder à la page d'accueil : http://localhost:8000
2. Cliquer sur "Lettings"
3. Parcourir la liste des locations disponibles
4. Cliquer sur une location pour voir les détails (adresse complète)

Cas d'usage 2 : Consulter les profils
--------------------------------------

1. Accéder à la page d'accueil
2. Cliquer sur "Profiles"
3. Parcourir la liste des utilisateurs
4. Cliquer sur un profil pour voir les informations (nom, email, ville favorite)

Cas d'usage 3 : Administration
-------------------------------

Ajouter une nouvelle location
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Accéder à http://localhost:8000/admin
2. Se connecter avec les identifiants admin
3. Aller dans "Addresses"
4. Cliquer "Add address" et remplir le formulaire
5. Aller dans "Lettings"
6. Cliquer "Add letting"
7. Choisir l'adresse créée et ajouter un titre

Ajouter un nouveau profil
^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Accéder à http://localhost:8000/admin
2. Aller dans "Users" et créer un utilisateur
3. Aller dans "Profiles"
4. Cliquer "Add profile"
5. Associer l'utilisateur et ajouter une ville favorite (optionnel)

Cas d'usage 4 : Tests et développement
---------------------------------------

Lancer les tests
^^^^^^^^^^^^^^^^

.. code-block:: bash

   pytest --cov

Vérifier le linting
^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   flake8

Déclencher une erreur Sentry (test)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Accéder à http://localhost:8000/sentry-debug/

L'erreur apparaîtra dans le dashboard Sentry.