# Find Duplicates in an Array

def find_duplicates(self, arr):
    seen, dup = set(), set()
    for num in arr:
        if num in seen:
            dup.add(num)
        seen.add(num)
    return list(dup)