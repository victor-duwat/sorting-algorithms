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

def display_color_pie(color_list):
    # Normalize RGB values to the range [0, 1]
    normalized_colors = [(r/255, g/255, b/255) for r, g, b in color_list]
    
    # Create a list of sizes for the pie chart
    # Assuming each color should have an equal size, you can adjust this as needed
    sizes = [1] * len(normalized_colors)
    
    # Create a pie chart
    plt.pie(sizes, colors=normalized_colors)
    
    # Equal aspect ratio ensures that pie is drawn as a circle
    plt.axis('equal')
    
    # Show the plot
    plt.show()

# Display the color pie
display_color_pie(sorted_array)