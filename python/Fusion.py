def fusion(L1, L2):
    if len(L1) == 0:
        return L2
    if len(L2) == 0:
        return L1
    
    result = []
    index_L1 = index_L2 = 0
    
    while len(result) < len(L1) + len(L2):
        if L1[index_L1] < L2[index_L2]:
            result.append(L1[index_L1])
            index_L1 += 1
        else:
            result.append(L2[index_L2])
            index_L2 += 1
        
        if index_L1 == len(L1):
            result.extend(L2[index_L2:])
            break
        if index_L2 == len(L2):
            result.extend(L1[index_L1:])
            break
    
    return result

def fusion_sort(liste):
    if len(liste) <= 1:
        return liste
    
    middle = len(liste) // 2
    left_half = fusion_sort(liste[:middle])
    right_half = fusion_sort(liste[middle:])
    
    return fusion(left_half, right_half)