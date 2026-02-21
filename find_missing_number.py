# Find the Missing Number: Find the missing number in an array of size n containing numbers from 1 to n.

class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        expected = n*(n+1)//2
        actual = sum(nums)
        return expected-actual
# TC: O(n)
# SC: O(1)

# Example Walkthrough

#Input: nums = [3,0,1]
# n = 3
# Expected sum = 3 * 4 / 2 = 6
# Actual sum = 3 + 0 + 1 = 4
# Missing = 6 - 4 = 2
# Output: 2
