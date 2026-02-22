# Find Peak Element: A peak element is greater than its neighbors. Find one such element.

# Using binary search

class Solution(object):
    def findPeakElement(self, nums):
        l, r = 0, len(nums)-1
        while l<r:
            mid = (l+r)//2
            if nums[mid]>nums[mid+1]:
                r = mid
            else:
                l = mid+1    
        return l        

# Example Walkthrough

# Input: nums = [1, 2, 3, 1]
# left = 0, right = 3
# mid = 1 → nums[1] = 2, nums[2] = 3
# Since 2 < 3, move right → left = 2

# Now left = 2, right = 3

# mid = 2 → nums[2] = 3, nums[3] = 1
# Since 3 > 1, move left → right = 2
# Loop ends → return 2
# Output: 2 (index of peak element 3)    
