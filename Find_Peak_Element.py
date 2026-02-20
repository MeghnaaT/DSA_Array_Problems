# Find Peak Element: A peak element is greater than its neighbors. Find one such element.

def find_peak(arr):
    for i in range(len(arr)):
        if (i == 0 or arr[i] > arr[i-1]) and \
           (i == len(arr)-1 or arr[i] > arr[i+1]):
            return i