import tkinter as tk
import random
import time
from Quick import QuickSort
from Bubble import bubble_sort
from Comb import comb_sort
from Fusion import fusion_sort
from Heapsort import heapsort
from Selection import selection_sort
from Insertion import insertion_sort

def generate_random_list():
    # Récupérer le nombre saisi par l'utilisateur
    num = int(entry.get())
    # Générer une liste aléatoire de la même longueur
    random_list = [random.randint(1, 100) for _ in range(num)]
    
    # Trier la liste avec chaque méthode de tri et mesurer le temps d'exécution
    results = []
    for sort_func in [bubble_sort, comb_sort, fusion_sort, heapsort, selection_sort, insertion_sort]:
        start_time = time.time()
        sorted_list = sort_func(random_list.copy())
        end_time = time.time()
        execution_time = end_time - start_time
        results.append((sorted_list, execution_time))
    
    # Afficher le résultat trié et le temps d'exécution
    result_text = "Liste triée: " + str(results[0][0]) + "\n\n"
    for sort_func, (sorted_list, execution_time) in zip([bubble_sort, comb_sort, fusion_sort, heapsort, selection_sort, insertion_sort, QuickSort(random_list.copy()).sort], results):
        result_text += f"{sort_func.__name__}: {execution_time:.5f} secondes\n"
    list_label.config(text=result_text)

# Créer la fenêtre principale
root = tk.Tk()
root.title("Générateur de liste aléatoire et tri")

# Créer un label et un champ de saisie pour le nombre
num_label = tk.Label(root, text="Entrez un nombre:")
num_label.pack()
entry = tk.Entry(root)
entry.pack()

# Créer un bouton pour générer la liste aléatoire et la trier
generate_button = tk.Button(root, text="Générer et trier la liste", command=generate_random_list)
generate_button.pack()

# Créer un label pour afficher le résultat
list_label = tk.Label(root, text="")
list_label.pack()

# Lancer la boucle principale de l'interface graphique
root.mainloop()