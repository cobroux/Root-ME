Le challenge : https://www.root-me.org/fr/Challenges/Web-Serveur/HTTP-Redirection-invalide

Ce challenge demande du réflexe 

En lançant le site : /web-serveur/ch32/
On remarque qu'un 2e chargement est éffectué vers /web-serveur/ch32/login.php?redirect 

En utilisant l'intercepter de Burp on peut stopper cette redirection est chopé le code source de la premiere page ainsi que le flag 