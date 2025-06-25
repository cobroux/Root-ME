Le challenge : https://www.root-me.org/fr/Challenges/Web-Serveur/HTTP-Open-redirect

Ici, on peut remarquer qu'il existe 3 liens avec un hash de validation pour le serveur 
Exemple:

‘‘‘
<a href="?url=https://facebook.com&amp;h=a023cfbf5f1c39bdf8407f28b60cd134">facebook</a>
‘‘‘

On peut deviner ici que le hash est le nom du site en MD5

Encore avec le curl 
‘‘‘
curl -G http://challenge01.root-me.org/web-serveur/ch52/ -d "url=https://google.fr&h=0edf27c83d4aa4699c0625d27be0e371" -o rootme.txt
‘‘‘

Ici -G et -d va permettre d'envoyer des données en GET et -o va recevoir dans un fichier text la réponse 

Ou bien avec BURP 

On récupére dans le proxy la requete quete du lien 
On injecte notre URL + hash dans le repeater

‘‘‘ 
GET /web-serveur/ch52/?url=https://google.fr&h=0edf27c83d4aa4699c0625d27be0e371
‘‘‘

Et la réponse nous donne notre flag !