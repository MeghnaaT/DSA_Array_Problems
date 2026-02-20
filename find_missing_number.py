# Find the Missing Number: Find the missing number in an array of size n containing numbers from 1 to n.

def find_missing_number(self, arr):
    n= len(arr)+1
    return n*(n+1)//2 - sum(arr)
