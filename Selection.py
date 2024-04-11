import time
from liste import generer_liste

def saisir_liste():
    liste = []
    while len(liste) < 10:  # Nous gardons la taille de la liste à 10 pour des raisons de démonstration
        try:
            chiffre = int(input("Entrez un chiffre : "))
            liste.append(chiffre)
        except ValueError:
            print("Veuillez entrer un chiffre valide.")
    return liste

choix = input("Voulez-vous générer une liste aléatoire (O/n) ? ").lower()

if choix == "o" or choix == "":
    L1 = generer_liste()
else:
    print("Entrez votre propre liste de chiffres (10 chiffres) :")
    L1 = saisir_liste()

def tri_selection(L1):
    start_time = time.time()
    for i in range(len(L1)):
        min_index = i
        for j in range(i + 1, len(L1)):
            if L1[j] < L1[min_index]:
                min_index = j
        L1[i], L1[min_index] = L1[min_index], L1[i]

    end_time = time.time()  
    elapsed_time = end_time - start_time 
    return elapsed_time  

print("L1 non triée :", L1)

tri_selection(L1)
temps_execution = tri_selection(L1)

print("\nL1 triée :\n", L1)
print("Temps d'exécution de l'algorithme de tri par Selection :\n", temps_execution, "secondes")
