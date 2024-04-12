import matplotlib.pyplot as plt
import matplotlib
import numpy as np

def display_color_bar(color_list):
    # Normalize RGB values to the range [0, 1]
    normalized_colors = [(r/255, g/255, b/255) for r, g, b in color_list]
    
    # Convert normalized RGB colors to HSV
    hsv_colors = [matplotlib.colors.rgb_to_hsv(color) for color in normalized_colors]
    
    # Sort colors based on hue and saturation
    sorted_colors = sorted(hsv_colors, key=lambda x: (x[0], x[1]))
    
    # Convert sorted HSV colors back to RGB
    sorted_rgb_colors = [matplotlib.colors.hsv_to_rgb(color) for color in sorted_colors]
    
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Set the y-axis to have a single tick at 0.5 (center of the bar)
    ax.set_yticks([0.5])
    ax.set_yticklabels(['']) # No label for the y-axis
    
    # Create a list of x positions for the bars
    x_positions = np.arange(len(sorted_rgb_colors))
    
    # Create a bar for each color in the sorted list
    for i, color in enumerate(sorted_rgb_colors):
        ax.bar(i, 1, color=color, edgecolor='black')
    
    # Remove the top and right spines from the plot
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    # Show the plot
    plt.show()

# Your list of RGB color codes
color_list = [(0, 0, 99), (2, 67, 229), (8, 5, 160), (8, 67, 103), (8, 216, 50), (12, 215, 216), (16, 130, 37), (20, 230, 119), (22, 217, 186), (23, 242, 109), (24, 218, 220), (25, 229, 161), (26, 117, 126), (26, 172, 110), (31, 21, 181), (36, 192, 155), (51, 140, 124), (55, 249, 65), (63, 255, 182), (65, 214, 211), (67, 39, 67), (67, 77, 182), (67, 146, 198), (71, 225, 242), (74, 125, 142), (76, 254, 232), (77, 76, 248), (78, 216, 219), (81, 133, 83), (90, 170, 72), (94, 48, 199), (97, 255, 19), (101, 56, 239), (106, 53, 176), (106, 91, 128), (110, 101, 191), (115, 210, 191), (117, 66, 30), (119, 10, 170), (123, 8, 46), (126, 213, 210), (130, 187, 135), (131, 177, 178), (135, 133, 243), (155, 112, 171), (156, 66, 37), (161, 153, 206), (163, 116, 237), (169, 132, 126), (171, 195, 127), (171, 219, 234), (174, 241, 92), (177, 55, 165), (177, 61, 65), (178, 36, 28), (180, 118, 86), (184, 25, 53), (190, 199, 168), (194, 209, 60), (195, 39, 135), (203, 210, 46), (209, 6, 121), (214, 169, 10), (215, 73, 177), (218, 141, 63), (221, 150, 189), (224, 116, 190), (224, 119, 186), (230, 200, 175), (230, 213, 134), (235, 204, 184), (235, 210, 16), (241, 8, 221), (241, 188, 208), (243, 247, 140), (245, 170, 165), (252, 141, 146), (255, 3, 147)]

list = []
for i in range (256) :
    list.append ((i, 80, 80))

print (list)

# Display the color bar
display_color_bar(color_list)

