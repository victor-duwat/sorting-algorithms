def tri_bulle(liste):
    n = len(liste)
    for i in range(n):
        for j in range(0, n-i-1):
            # Si l'élément trouvé est plus grand que le suivant, on les échange
            if liste[j] > liste[j+1] :
                liste[j], liste[j+1] = liste[j+1], liste[j]
    return liste

# Exemple d'utilisation
liste_entiers_str = input("Entrez une liste d'entiers séparés par des espaces : ")
liste_entiers = [int(x) for x in liste_entiers_str.split()]
liste_triee = tri_bulle(liste_entiers)
liste_triee = tri_bulle(liste_entiers)
print("Liste triée :", liste_triee)