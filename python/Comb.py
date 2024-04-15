def comb_sort(liste):
    # Initializing the comparison interval
    intervalle = len(liste)
    # Reduced comparison interval at each iteration
    while intervalle > 1:
        intervalle = int(intervalle // 1.3) # Convert interval to integer after splitting
        for i in range(len(liste) - intervalle):
            if liste[i] > liste[i + intervalle]:
                liste[i], liste[i + intervalle] = liste[i + intervalle], liste[i]
    return liste