# Find Maximum Difference (j > i)

def max_difference(arr):
    min_val = arr[0]
    max_diff = float('-inf')
    for num in arr[1:]:
        max_diff = max(max_diff, num - min_val)
        min_val = min(min_val, num)
    return max_diff