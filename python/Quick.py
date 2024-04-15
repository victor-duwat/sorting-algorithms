def partition(array, low, high):
    i = (low-1)
    pivot = array[high]

    for j in range(low, high):
        if array[j] <= pivot:
            i = i+1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return (i+1)

def quick_sorting(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sorting(array, low, pi-1)
        quick_sorting(array, pi+1, high)

def quick_sort(array):
    n = len(array)
    quick_sorting(array, 0, n-1)
    return array