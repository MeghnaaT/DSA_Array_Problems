# Remove given Element from Array

# 2 pointer

class Solution:
    def removeElement(self, nums, val):
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

# TC: O(n)
# SC: O(1)

# Example Walkthrough

# Input: nums = [3,2,2,3], val = 3

# Start: i=0
# j=0: nums[0]=3 → skip
# j=1: nums[1]=2 ≠ 3 → place at nums[0], array becomes [2,2,2,3], i=1
# j=2: nums[2]=2 ≠ 3 → place at nums[1], array becomes [2,2,2,3], i=2
# j=3: nums[3]=3 → skip
# Return i=2.
# First 2 elements are [2,2]. The rest doesn’t matter.
