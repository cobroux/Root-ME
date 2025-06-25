Le challenge : https://www.root-me.org/fr/Challenges/Web-Serveur/HTTP-Headers

par moment il suffit juste de regarder les headers 

Avec burp on peut voir dans la réponse http
‘‘‘
Header-RootMe-Admin: none 
‘‘‘

Si mal configuré on peut changer cette info via le même get en y rajoutant 

‘‘‘
Header-RootMe-Admin: "admin"
‘‘‘