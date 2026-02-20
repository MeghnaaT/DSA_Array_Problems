# Find Maximum Product Pair: Find two elements whose product is maximum.

def max_product_pair(arr):
    arr.sort()
    return max(arr[-1]*arr[-2], arr[0]*arr[1])