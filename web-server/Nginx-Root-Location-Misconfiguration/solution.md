Le challenge : https://www.root-me.org/fr/Challenges/Web-Serveur/Nginx-Root-Location-Misconfiguration

Encore une faille nginx :) 

Par moment on peut voir le fichier de config à la racine si le serveur est mal configuré 

‘‘‘
nginx.conf
‘‘‘

Ce fichier va nous montrer certaines ressources intérrésantes dont une configuration importé 

‘‘‘
include /etc/nginx/conf.d/default.conf;
‘‘‘

en cherchant dans l'url 
‘‘‘
conf.d/default.conf
‘‘‘
On obtient le flag 