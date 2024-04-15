def comb_sort(liste):
    # Initialisation de l'intervalle de comparaison
    intervalle = len(liste)
    # Réduction de l'intervalle de comparaison à chaque itération
    while intervalle > 1:
        intervalle = int(intervalle // 1.3) # Convertir l'intervalle en entier après la division
        for i in range(len(liste) - intervalle):
            if liste[i] > liste[i + intervalle]:
                liste[i], liste[i + intervalle] = liste[i + intervalle], liste[i]
    return liste