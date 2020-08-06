# Dockerized-Django-App

Pour lancer l'application :

* lancer la commande : "docker-compose up" dans le dossier "PROJECT"

* aller sur un navigateur et taper le lien : http://localhost:8000/

* Vous devriez tomber sur le site demandé

- Il y a deux points à souligner :
* Il n'y a pas de page d'accueil. Il faut directement accéder au lien http://localhost:8000/register pour s'inscrire, on est ensuite redirigé dans la page de connexion.
* On peut bien modifier l'adresse mail (dans la base de données) cependant, l'affichage sur la page se modifie qu'après un rechargement de la page.
