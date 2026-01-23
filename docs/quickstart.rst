Guide de démarrage rapide
==========================

Lancer le serveur de développement
-----------------------------------

.. code-block:: bash

   python manage.py runserver

Le site est accessible sur http://localhost:8000

Accéder à l'interface d'administration
---------------------------------------

URL : http://localhost:8000/admin

Identifiants de test :

* Utilisateur : ``admin``
* Mot de passe : ``Abc1234!``

Lancer les tests
----------------

.. code-block:: bash

   pytest

Vérifier la couverture de tests
--------------------------------

.. code-block:: bash

   pytest --cov=. --cov-report=term-missing

Lancer le linting
-----------------

.. code-block:: bash

   flake8