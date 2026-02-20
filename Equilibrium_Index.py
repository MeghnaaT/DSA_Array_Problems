# Find Equilibrium Index: Find an index such that sum of elements on left = sum on right.

def equilibrium_index(arr):
    total = sum(arr)
    left = 0
    for i, num in enumerate(arr):
        if left == total - left - num:
            return i
        left += num
    return -1