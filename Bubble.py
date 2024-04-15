def bubble_sort(liste):
    n = len(liste)
    for i in range(n):
        for j in range(0, n-i-1):
            # Si l'élément trouvé est plus grand que le suivant, on les échange
            if liste[j] > liste[j+1] :
                liste[j], liste[j+1] = liste[j+1], liste[j]
    return liste

