from random import randint, sample
import time

def random_color_generator(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    
    # Calculate the total number of possible unique RGB colors
    total_colors = 256**3
    
    if n > total_colors:
        raise ValueError("n cannot be greater than the total number of possible unique RGB colors")
    
    # Generate n unique random colors
    color_list = []
    while len(color_list) < n:
        # Generate a random color
        r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
        color = (r, g, b)
        
        # Add the color to the list if it's not already there
        if color not in color_list:
            color_list.append(color)
    
    return color_list

# Example usage
generated_color = (random_color_generator(78))
print(generated_color)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from Tri_rapide import QuickSort

quick_sort = QuickSort (generated_color)

start_time = time.time() # Capture the start time
sorted_array = quick_sort.sort()
end_time = time.time() # Capture the end time

print ("\nsorted :\n")
print (sorted_array)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

def display_color_pie(unsorted_color_list, sorted_color_list):
    # Normalize RGB values to the range [0, 1] for both lists
    normalized_unsorted_colors = [(r/255, g/255, b/255) for r, g, b in unsorted_color_list]
    normalized_sorted_colors = [(r/255, g/255, b/255) for r, g, b in sorted_color_list]
    
    # Create a list of sizes for the pie chart
    # Assuming each color should have an equal size, you can adjust this as needed
    sizes = [1] * len(normalized_unsorted_colors)
    
    # Create a figure with two subplots
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    
    # Create a pie chart for the unsorted colors
    axs[0].pie(sizes, colors=normalized_unsorted_colors)
    axs[0].set_title('Non trié')
    axs[0].axis('equal')
    
    # Create a pie chart for the sorted colors
    axs[1].pie(sizes, colors=normalized_sorted_colors)
    axs[1].set_title('Trié')
    axs[1].axis('equal')
    
    # Show the plot
    plt.show()

# Display the color pie for both unsorted and sorted lists
display_color_pie(generated_color, sorted_array)
