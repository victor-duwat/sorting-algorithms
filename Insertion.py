def insertion_sort(liste):
    for i in range(1, len(liste)):
        valeur_a_inserer = liste[i]
        position = i

        while position > 0 and liste[position - 1] > valeur_a_inserer:
            liste[position] = liste[position - 1]
            position = position - 1

        liste[position] = valeur_a_inserer

    return liste