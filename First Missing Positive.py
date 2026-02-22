# Find the First Missing Positive: Find the smallest positive integer missing in the array.

class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)
    
    # Place each number in its correct position
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
    
    # Find the first missing positive
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
    
        return n + 1

# Example Walkthrough

# Input: nums = [3,4,-1,1]

# Rearrangement:
# Place 3 at index 2 → [ -1, 4, 3, 1 ]
# Place 1 at index 0 → [ 1, 4, 3, -1 ]
# Final array: [1, -1, 3, 4]

# Scan:

# nums[0] = 1 ✅
# nums[1] = -1 ❌ → return 2
# Output: 2
