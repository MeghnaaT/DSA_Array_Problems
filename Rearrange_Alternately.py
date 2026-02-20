# Rearrange Array Alternately: Rearrange an array such that elements alternate between the largest and smallest.

def rearrange_alternate(arr):
    arr.sort()
    result = []
    i, j = 0, len(arr)-1
    while i <= j:
        if i != j:
            result.extend([arr[j], arr[i]])
        else:
            result.append(arr[i])
        i += 1
        j -= 1
    return result