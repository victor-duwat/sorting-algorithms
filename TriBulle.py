from liste import generer_liste
import time

def tri_bulle(liste):
    n = len(liste)
    for i in range(n):
        for j in range(0, n-i-1):
            # Si l'élément trouvé est plus grand que le suivant, on les échange
            if liste[j] > liste[j+1] :
                liste[j], liste[j+1] = liste[j+1], liste[j]
    return liste

# Exemple d'utilisation
Liste = generer_liste()
Liste_trié = tri_bulle(Liste)

# Mesure du temps d'exécution
start_time = time.time()
Liste_trié = tri_bulle(Liste)
end_time = time.time()

execution_time = end_time - start_time
print(f"Temps d'exécution de tri_bulle : {execution_time} secondes")

