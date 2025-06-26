Le challenge : https://www.root-me.org/fr/Challenges/Web-Serveur/API-Broken-Access

Du swagger :)

Tout d'abord on va créer un user et ce logger grace aux endpoint 

Si on essaye de get un user 

on obtient 
Jamais ceux à 0 ou 1 

{
  "note": "",
  "userid": 2,
  "username": "aa"
}

Donc on supposera que l'admin et l'un des deux et avec vérification par création d'user on pourra remarquer qu'un admin existe 

Si on va sur Burp on peut forcer le GET avec l'id souhaité  
‘‘‘
GET /api/user/1
‘‘‘

On remarquera que notre admin est bien la avec son flag
