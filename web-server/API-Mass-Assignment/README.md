Le challenge : https://www.root-me.org/fr/Challenges/Web-Serveur/API-Mass-Assignment

retour sur le swagger de broken access qui est amélioré (ou pas^^)

Pareil que la dernière fois on crée un utilisateur et on se log 

On remarque que maintenant le get api/user est fix et ne propose pas de demander un id 

Cependant on peut voir maintenant qu'il y a des roles 

‘‘‘
{
  "id": 0,
  "username": "string",
  "note": "string",
  "status": "string"
}
‘‘‘

Le swagger nous indique un get api/flag uniquement accessible par l'admin donc il va falloir changer notre status ^^

On essayera de modifier le get /api/user en put avec {user:, pwd:, status:}
On sera vite bloqué par 
‘‘‘
415 Unsupported Media Type
Did not attempt to load JSON data because the request Content-Type was not application/json.
‘‘‘

Il faudra juste rajouter dans notre PUT 

Content-Type:application/json

On aura un nouveau user 
on se connecte 
et le flag est à nous ^^