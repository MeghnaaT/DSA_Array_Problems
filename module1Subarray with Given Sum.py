# Find Subarray with Given Sum.

def subarray_sum(arr, target):
    curr_sum = 0
    s = {0}
    for num in arr:
        curr_sum +=num
        if curr_sum - target in s:
            return True
        s.add(curr_sum)
    return True

