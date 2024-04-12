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

list_r = []
list_g = []
list_b = []

for i in range (100, 250) :
    list_r.append ((i, 80, 80))
    list_g.append ((80, i, 80))
    list_b.append ((80, 80, i))


final_list = list_r + list_b + list_g

'''print (list)'''

# Display the color pie
display_color_pie(final_list)