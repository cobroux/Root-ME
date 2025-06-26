Le challenge : https://www.root-me.org/fr/Challenges/Web-Serveur/Insecure-Code-Management

Sur le site de challenge on peut s'appercevoir qu'il existe un .git on va récupérer le projet 

On va utiliser cette outil 
https://github.com/internetwache/GitTools/

Tout d'abord le Dumper pour aller télécharger notre projet 

'''
dumper.sh https://site/.git/ <rep_cible>
'''


Maintenant qu'on à notre .git installé on peut se balader 

On peut voir les log avec git log, on s'apperçoit de modification sur le pwd 
On va restorer le commit

En effectuant un git status on s'appercoit que le dernier commit a supprimé des choses intéréssantes 

On va faire git revert HEAD et hop config.php et le flag