def heapify(liste, n, i):
    """
    Fonction pour ajuster la structure du tas
    """
    plus_grand = i # Initialiser le plus grand comme le noeud racine
    gauche = 2 * i + 1
    droite = 2 * i + 2

    # Si le noeud gauche est plus grand que le noeud racine
    if gauche < n and liste[gauche] > liste[plus_grand]:
        plus_grand = gauche

    # Si le noeud droit est plus grand que le noeud le plus grand trouvé jusqu'à présent
    if droite < n and liste[droite] > liste[plus_grand]:
        plus_grand = droite

    # Si le noeud le plus grand n'est pas le noeud racine
    if plus_grand != i:
        liste[i], liste[plus_grand] = liste[plus_grand], liste[i] # Échanger

        # Heapify le sous-arbre réduit
        heapify(liste, n, plus_grand)

def tri_par_tas(liste):
    n = len(liste)

    # Construire le tas
    for i in range(n, -1, -1):
        heapify(liste, n, i)

    # Extraire un par un les éléments du tas
    for i in range(n-1, 0, -1):
        liste[i], liste[0] = liste[0], liste[i] # Échanger
        heapify(liste, i, 0)

    return liste

# Demande à l'utilisateur d'entrer une liste d'entiers séparés par des espaces
liste_entiers_str = input("Entrez une liste d'entiers séparés par des espaces : ")

# Convertit la chaîne de caractères en une liste d'entiers
liste_entiers = [int(x) for x in liste_entiers_str.split()]

# Tri la liste d'entiers
liste_triee = tri_par_tas(liste_entiers)

# Affiche la liste triée
print("Liste triée :", liste_triee)