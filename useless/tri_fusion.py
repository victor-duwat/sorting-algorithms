from useless.list_creator import ListeCreator
import time # Import the time module


def fusion(gauche, droite):
    """Fusionne deux listes triées en une seule liste triée."""
    resultat = []
    i = j = 0

    # Tant que nous avons des éléments dans les deux listes
    while i < len(gauche) and j < len(droite):
        if gauche[i] < droite[j]:
            resultat.append(gauche[i])
            i += 1
        else:
            resultat.append(droite[j])
            j += 1

    # Si des éléments restent dans la liste de gauche, les ajouter
    while i < len(gauche):
        resultat.append(gauche[i])
        i += 1

    # Si des éléments restent dans la liste de droite, les ajouter
    while j < len(droite):
        resultat.append(droite[j])
        j += 1

    return resultat

def tri_par_fusion(liste):
    """Effectue le tri par fusion sur la liste donnée."""
    if len(liste) <= 1:
        return liste

    milieu = len(liste) // 2
    gauche = tri_par_fusion(liste[:milieu])
    droite = tri_par_fusion(liste[milieu:])

    return fusion(gauche, droite)

# Exemple d'utilisation
liste_non_tries = ListeCreator.create_random_array(5000000)


start_time = time.time() # Capture the start time
liste_tries = tri_par_fusion(liste_non_tries)
end_time = time.time() # Capture the end time

print("Array après tri :", liste_tries)
print("Temps d'exécution :", end_time - start_time, "secondes") # Calculate and print the execution time