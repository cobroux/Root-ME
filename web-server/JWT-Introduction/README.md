Le challenge : https://www.root-me.org/fr/Challenges/Web-Serveur/JWT-Introduction#validation_challenge


Tout d'abord qu'est ce que JWT ?
Un JWT (JSON Web Token) est un format compact, sécurisé et encodé utilisé pour transmettre des informations entre deux parties (typiquement un client et un serveur) de manière fiable et signée.

En explorant le site on peut voir qu'on peut se connecter en guest donc on va essayer d'être admin 

Dans burp on peut voir rapidement un POST et un échange de cookie 

Le cookie est en 3 partie (header, payload, signature)

{"typ":"JWT","alg":"HS256"} . {"username":"guest"} . SIGNATURE 

Le but ici on l'aura deviné est de tronquer cette url qui est en base64 

On va essayer ça 
l'algo sur none car il y a une faille ici potentiel et on veut être admin 
{"typ":"JWT","alg":"none"} . {"username":"admin"} . SIGNATURE 

Hop ça marche 


