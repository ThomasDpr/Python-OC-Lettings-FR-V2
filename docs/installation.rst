Instructions d'installation
===========================

Prérequis
---------

* Python 3.11 ou supérieur
* Git
* Un environnement virtuel Python

Installation locale
-------------------

Cloner le repository
^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   git clone https://github.com/ThomasDpr/Python-OC-Lettings-FR-V2.git
   cd Python-OC-Lettings-FR-V2

Créer l'environnement virtuel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   # ou
   .\venv\Scripts\activate  # Windows

Installer les dépendances
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   pip install -r requirements.txt

Configuration
-------------

Créer un fichier ``.env`` à la racine du projet :

.. code-block:: bash

   SECRET_KEY=votre-secret-key-developpement
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   SENTRY_DSN=votre-sentry-dsn-optionnel

Migrations de base de données
------------------------------

.. code-block:: bash

   python manage.py migrate

Créer un superutilisateur (optionnel)
--------------------------------------

.. code-block:: bash

   python manage.py createsuperuser