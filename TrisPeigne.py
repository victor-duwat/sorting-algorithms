from liste import generer_liste
import time



def tri_a_peigne(liste):
    # Initialisation de l'intervalle de comparaison
    intervalle = len(liste)
    # Réduction de l'intervalle de comparaison à chaque itération
    while intervalle > 1:
        intervalle = int(intervalle // 1.3) # Convertir l'intervalle en entier après la division
        for i in range(len(liste) - intervalle):
            if liste[i] > liste[i + intervalle]:
                liste[i], liste[i + intervalle] = liste[i + intervalle], liste[i]
    return liste

# Génération d'une liste de nombres aléatoires
Liste = generer_liste()

# Mesure du temps d'exécution
start_time = time.time()
Liste_triée = tri_a_peigne(Liste)
end_time = time.time()

execution_time = end_time - start_time
print(f"Temps d'exécution de tri_a_peigne : {execution_time} secondes")
