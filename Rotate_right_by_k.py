# Rotate Array by k Positions: Rotate the array to the right by k positions.

def rotate_right(arr,k):
    k %= len(arr) # % ensures that k is within the bounds of array's length
    return arr[-k:] + arr[:-k]

# arr[-k:] = slices the array to get the last k elements
# arr[:-k] = slices the array to get all elements except the last k elements
# TC : O(n)

# Example:
# If arr = [1, 2, 3, 4, 5] and k = 2:
# k %= len(arr) becomes 2 %= 5, so k remains 2.
# arr[-k:] becomes arr[-2:], which is [4, 5].
# arr[:-k] becomes arr[:-2], which is [1, 2, 3].
# The function returns [4, 5] + [1, 2, 3], resulting in the rotated array [4, 5, 1, 2, 3].