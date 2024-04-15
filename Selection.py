def selection_sort(L1):
    for i in range(len(L1)):
        min_index = i
        for j in range(i + 1, len(L1)):
            if L1[j] < L1[min_index]:
                min_index = j
        L1[i], L1[min_index] = L1[min_index], L1[i]
    return L1