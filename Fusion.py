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

def fusion(L1, L2):
    if len(L1) == 0:
        return L2
    if len(L2) == 0:
        return L1
    
    result = []
    index_L1 = index_L2 = 0
    
    while len(result) < len(L1) + len(L2):
        if L1[index_L1] < L2[index_L2]:
            result.append(L1[index_L1])
            index_L1 += 1
        else:
            result.append(L2[index_L2])
            index_L2 += 1
        
        if index_L1 == len(L1):
            result.extend(L2[index_L2:])
            break
        if index_L2 == len(L2):
            result.extend(L1[index_L1:])
            break
    
    return result

def tri_fusion(liste):
    if len(liste) <= 1:
        return liste
    
    middle = len(liste) // 2
    left_half = tri_fusion(liste[:middle])
    right_half = tri_fusion(liste[middle:])
    
    return fusion(left_half, right_half)

print("L1 non triée :", L1)

start_time = time.time()
L1_triee = tri_fusion(L1)
end_time = time.time()

temps_execution = end_time - start_time

print("L1 triée :", L1_triee)
print("Temps d'exécution de l'algorithme de tri par fusion :", temps_execution, "secondes")
