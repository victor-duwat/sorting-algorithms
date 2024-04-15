import tkinter as tk
import random
import time
from python.Quick import quick_sort
from python.Bubble import bubble_sort
from python.Comb import comb_sort
from python.Fusion import fusion_sort
from python.Heapsort import heapsort
from python.Selection import selection_sort
from python.Insertion import insertion_sort

def generate_random_list():
    # Retrieve the number entered by the user
    num = int(entry.get())
    # Generate a random list of the same length
    random_list = [random.randint(1, 100) for _ in range(num)]
    
    # Sort the list with each sorting method and measure the execution time
    results = []
    for sort_func in [bubble_sort, comb_sort, fusion_sort, heapsort, selection_sort, insertion_sort, quick_sort]:
        start_time = time.time()
        sorted_list = sort_func(random_list.copy())
        end_time = time.time()
        execution_time = end_time - start_time
        results.append((sorted_list, execution_time))
    
    # Display the sorted result and the execution time
    result_text = "Sorted list: " + str(results[0][0]) + "\n\n"
    for sort_func, (sorted_list, execution_time) in zip([bubble_sort, comb_sort, fusion_sort, heapsort, selection_sort, insertion_sort, quick_sort], results):
        result_text += f"{sort_func.__name__}: {execution_time:.5f} secondes\n"
    list_label.config(text=result_text)

# Create the main window
root = tk.Tk()
root.title("Random List Generator and Sorter")

# Create a label and an entry field for the number
num_label = tk.Label(root, text="Enter a number:")
num_label.pack()
entry = tk.Entry(root)
entry.pack()

# Create a button to generate the random list and sort it
generate_button = tk.Button(root, text="Generate and sort the list", command=generate_random_list)
generate_button.pack()

# Create a label to display the result
list_label = tk.Label(root, text="")
list_label.pack()

# Start the main GUI loop
root.mainloop()