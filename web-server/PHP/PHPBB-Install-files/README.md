Le challenge : https://www.root-me.org/fr/Challenges/Web-Serveur/Install-files

Une faille très courante est l’oubli de fichiers d’installation de framework php dans l’arborescence web. 
Ici, on regarde le code source de la page http://challenge.root-me.org/web-serveur/ch6/ On y trouve un commentaire HTML :
/web-serveur/ch6/phpbb

On peut vite trouver que le fichier d'installation est "/install/install.php".

On demande la page /web-serveur/ch6/phpbb/install/install.php

Et hop le flag est obtenue 