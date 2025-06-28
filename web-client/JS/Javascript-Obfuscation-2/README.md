Le challenge : https://www.root-me.org/fr/Challenges/Web-Client/Javascript-Obfuscation-2

En fouillant le code on voit ça 

```
	var pass = unescape("unescape%28%22String.fromCharCode%2528104%252C68%252C117%252C102%252C106%252C100%252C107%252C105%252C49%252C53%252C54%2529%22%29");
```
Après premier unescape 
```
Soit unscape(unescape("String.fromCharCode%28104%2C68%2C117%2C102%2C106%2C100%2C107%2C105%2C49%2C53%2C54%29"))
```
Deuxieme 
```
String.fromCharCode(104,68,117,102,106,100,107,105,49,53,54)
```

Et hop le mdp


