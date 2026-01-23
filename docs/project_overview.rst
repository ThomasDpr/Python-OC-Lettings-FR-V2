Description du projet
=====================

Contexte
--------

Orange County Lettings est une start-up en phase d'expansion dans le secteur de la location immobilière aux États-Unis.

Objectifs du projet
-------------------

Ce projet a pour but de :

* Refactoriser l'architecture monolithique en architecture modulaire
* Mettre en place un pipeline CI/CD automatisé
* Déployer l'application en production
* Surveiller les erreurs avec Sentry
* Améliorer la qualité du code (tests, linting, documentation)

Architecture
------------

L'application est structurée en 3 applications Django :

* **oc_lettings_site** : Application principale et configuration
* **lettings** : Gestion des locations et adresses
* **profiles** : Gestion des profils utilisateurs