def heapify(liste, n, i):
    """
    Function to adjust the structure of the pile
    """
    plus_grand = i # Initialize the largest as the root node
    gauche = 2 * i + 1
    droite = 2 * i + 2

    # If the left node is larger than the root node
    if gauche < n and liste[gauche] > liste[plus_grand]:
        plus_grand = gauche

    # If the right node is larger than the largest node found so far
    if droite < n and liste[droite] > liste[plus_grand]:
        plus_grand = droite

    # If the largest node is not the root node
    if plus_grand != i:
        liste[i], liste[plus_grand] = liste[plus_grand], liste[i] # Switch

        # Heapify the reduced sub-shaft
        heapify(liste, n, plus_grand)

def heapsort(liste):
    n = len(liste)

    # Build the pile
    for i in range(n, -1, -1):
        heapify(liste, n, i)

    # Extract one by one the elements of the heap
    for i in range(n-1, 0, -1):
        liste[i], liste[0] = liste[0], liste[i] # switch
        heapify(liste, i, 0)

    return liste