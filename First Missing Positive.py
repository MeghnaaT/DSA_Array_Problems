# Find the First Missing Positive: Find the smallest positive integer missing in the array.

def first_missing_positive(arr):
    s = set(arr)
    i = 1
    while True:
        if i not in s:
            return i
        i += 1