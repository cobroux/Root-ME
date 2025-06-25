Le challenge : https://www.root-me.org/fr/Challenges/Web-Serveur/CRLF

En tappant dans le login et pwd on remarque qu'on écrit dans le log 

Donc le but va être de faire des /r/n pour écrire en plus dans le log 
‘‘‘
guest%20authenticated.%0d%0aexp&password=none
‘‘‘

Avec ça on pourra êcrire 
guest authenticated

Et 
exp&password=none qui affichera exp failed to authenticate.

%0d%0a correspond au retour
et %20 à un espace 

On fait croire ici que guest est co mais exp non 


