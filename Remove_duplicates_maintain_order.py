# Remove Duplicates from Array: Remove duplicates from the array while maintaining order.

def remove_duplicate(self, arr):
    seen = set()
    result = []

    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result
