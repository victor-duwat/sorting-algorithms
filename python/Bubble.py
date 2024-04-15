def bubble_sort(liste):
    n = len(liste)
    for i in range(n):
        for j in range(0, n-i-1):
            # if the item found is larger than the following, they are exchanged
            if liste[j] > liste[j+1] :
                liste[j], liste[j+1] = liste[j+1], liste[j]
    return liste

