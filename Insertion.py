import time
from liste import generer_liste

def saisir_liste():
    liste = []
    while len(liste) < 10:  
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

def tri_insertion(liste):
    for i in range(1, len(liste)):
        valeur_a_inserer = liste[i]
        position = i

        while position > 0 and liste[position - 1] > valeur_a_inserer:
            liste[position] = liste[position - 1]
            position = position - 1

        liste[position] = valeur_a_inserer

    return liste

print("L1 non triée :", L1)

start_time = time.time()
L1_triee = tri_insertion(L1)
end_time = time.time()

temps_execution = end_time - start_time

print("L1 triée :", L1_triee)
print("Temps d'exécution de l'algorithme de tri par insertion :", temps_execution, "secondes")
