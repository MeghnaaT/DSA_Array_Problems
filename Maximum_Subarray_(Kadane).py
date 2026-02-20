# Maximum Sum Subarray (Kadane's Algorithm)

def max_subarray(arr):
    curr = max_sum = arr[0]
    for num in arr[1:]:
        curr = max(num, curr+num)
        max_sum = max(max_sum, curr)
    return max_sum