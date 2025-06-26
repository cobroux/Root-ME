Le challenge : https://www.root-me.org/fr/Challenges/Web-Serveur/HTTP-Directory-indexing

Certains serveurs sont mal configurés au point ou on peut avoir accès à des dossiers 

Quand on inspect l'élément on tombe sur 

/admin/pass.html 

pass.html sera un prank mais ce qui nous interresse est admin en y accédant on y trouve un répertoire backup et un fichier txt avec le mdp :)


Une solution sugère l'utilisation de nikito 

nikto -h http://challenge01.root-me.org/web-serveur/ch4/

Nikito va scanner la cible pour des chemins à exploiter