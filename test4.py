def sort_tuples(tuples_list):
    # Initialize three empty lists for sorting
    list1 = []
    list2 = []
    list3 = []

    # Iterate over the list of tuples
    for tup in tuples_list:
        # Append elements to the corresponding list based on their index
        list1.append(tup)
        list2.append(tup)
        list3.append(tup)

    # Sort each list
    list1.sort(key=lambda x: x[0])
    list2.sort(key=lambda x: x[1])
    list3.sort(key=lambda x: x[2])

    # Return the three sorted lists
    return list1, list2, list3

# Example usage
tuples = [(3, 9, 8), (6, 5, 4), (9, 8, 2)]
sorted_lists = sort_tuples(tuples)
print(sorted_lists)