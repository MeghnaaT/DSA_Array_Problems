# Move Zeroes to End: Move all zeroes in an array to the end while maintaining the order of non-zero elements.

def move_zereos(self,arr):
    non_zero = [x for x in arr if x!=0]
    return non_zero + [0]*(len(arr) - len(non_zero))