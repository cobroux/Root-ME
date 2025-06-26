Le challenge : https://www.root-me.org/fr/Challenges/Web-Serveur/Nginx-Alias-Misconfiguration

Une faille courante de NGINX permet si mal configuré 

Via inspection on remarque un commentaire qui nous suggère le path /assets 

Ce répo https://github.com/shiblisec/Kyubi, peut nous montrer les alias qui peuvent mener à la découvertes d'alias qui peuvent nous révéler certain repertoires 

Donc via /assets../ et en fouillant on obtient facilement le flag
NB: Ce double . nous fait remonter d'un niveau 