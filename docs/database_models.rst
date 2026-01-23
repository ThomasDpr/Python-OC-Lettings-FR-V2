Structure de la base de données
================================

Application lettings
--------------------

Modèle Address
^^^^^^^^^^^^^^

Représente une adresse physique.

Champs :

* ``number`` : Numéro de rue (1-9999)
* ``street`` : Nom de la rue (max 64 caractères)
* ``city`` : Ville (max 64 caractères)
* ``state`` : État (2 lettres)
* ``zip_code`` : Code postal (1-99999)
* ``country_iso_code`` : Code pays ISO (3 lettres)

Modèle Letting
^^^^^^^^^^^^^^

Représente une location immobilière.

Champs :

* ``title`` : Titre de la location (max 256 caractères)
* ``address`` : Relation OneToOne vers Address

Application profiles
--------------------

Modèle Profile
^^^^^^^^^^^^^^

Représente le profil d'un utilisateur.

Champs :

* ``user`` : Relation OneToOne vers User (Django)
* ``favorite_city`` : Ville favorite (max 64 caractères, optionnel)

Schéma relationnel
------------------

.. code-block:: text

   User (Django) --[1:1]-- Profile
   
   Address --[1:1]-- Letting