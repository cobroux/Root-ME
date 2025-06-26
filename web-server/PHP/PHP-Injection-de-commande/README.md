Le challenge : https://www.root-me.org/fr/Challenges/Web-Serveur/PHP-Injection-de-commande

On remarque que si on saisie dans le form 127.0.0.1 comme indiqué 
On verra un ping éxécuté 
Donc par curiosité on peut sur certaine page PHP injecter du shell 

Si on essaye par exemple ;ls on voit que c'est bien interprété et on voit notre index.php

On peut aller plus loin 

On regarde ou on est et ce qu'il y a dedans donc 
;pwd ;ls -a

On remarque un .passwd

;cat passwd 
et hop le flag 
