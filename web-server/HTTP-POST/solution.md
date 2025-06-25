Le challenge : https://www.root-me.org/fr/Challenges/Web-Serveur/HTTP-POST

Ce site nous montre un bouton random qui va nous permettre d'essayer de battre le score maximal 
Spoiler-alert ça ne marchera jamais 

En regardant avec le proxy de burp on peut voir qu'un post est éffectué avec le nombre du boutton 

comme ceci : 
‘‘‘
score=141019&generate=Give+a+try%21
‘‘‘

Le but ici est avec le repeater d'envoyer le nombre souhaité et hop c'est gagné 