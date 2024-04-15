import time
from list_creator import ListeCreator

def partition(array, low, high):
    i = (low-1)
    pivot = array[high]

    for j in range(low, high):
        if array[j] <= pivot:
            i = i+1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return (i+1)

def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi-1)
        quick_sort(array, pi+1, high)

def sort_array(array):
    n = len(array)
    quick_sort(array, 0, n-1)
    return array

if __name__ == "__main__":
    array = ListeCreator.create_random_array(5000) # Use the function to create a random array
    
    start_time = time.time() # Capture the start time
    sorted_array = sort_array(array)
    end_time = time.time() # Capture the end time

    print("Array après tri :", sorted_array)
    print("Temps d'exécution :", end_time - start_time, "secondes") # Calculate and print the execution time