Interfaces de programmation
============================

URLs principales
----------------

Page d'accueil
^^^^^^^^^^^^^^

* **URL** : ``/``
* **Vue** : ``oc_lettings_site.views.index``
* **Template** : ``oc_lettings_site/index.html``
* **Description** : Page d'accueil du site

Application lettings
--------------------

Liste des lettings
^^^^^^^^^^^^^^^^^^

* **URL** : ``/lettings/``
* **Namespace** : ``lettings:index``
* **Vue** : ``lettings.views.index``
* **Template** : ``lettings/index.html``
* **Description** : Liste toutes les locations disponibles

Détail d'un letting
^^^^^^^^^^^^^^^^^^^

* **URL** : ``/lettings/<int:letting_id>/``
* **Namespace** : ``lettings:letting``
* **Vue** : ``lettings.views.letting``
* **Template** : ``lettings/letting.html``
* **Description** : Affiche les détails d'une location

Application profiles
--------------------

Liste des profils
^^^^^^^^^^^^^^^^^

* **URL** : ``/profiles/``
* **Namespace** : ``profiles:index``
* **Vue** : ``profiles.views.index``
* **Template** : ``profiles/index.html``
* **Description** : Liste tous les profils utilisateurs

Détail d'un profil
^^^^^^^^^^^^^^^^^^

* **URL** : ``/profiles/<str:username>/``
* **Namespace** : ``profiles:profile``
* **Vue** : ``profiles.views.profile``
* **Template** : ``profiles/profile.html``
* **Description** : Affiche le profil d'un utilisateur

Gestion des erreurs
-------------------

Erreur 404
^^^^^^^^^^

* **Handler** : ``oc_lettings_site.views.custom_404``
* **Template** : ``404.html``
* **Description** : Page personnalisée pour erreurs 404

Erreur 500
^^^^^^^^^^

* **Handler** : ``oc_lettings_site.views.custom_500``
* **Template** : ``500.html``
* **Description** : Page personnalisée pour erreurs 500