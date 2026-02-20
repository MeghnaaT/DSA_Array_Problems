# Rotate Array to the Left by k Positions

def rotate_left(arr, k):
    k %= len(arr)
    return arr[k:] + arr[:k]