# Sort an Array of 0s, 1s, and 2s: Sort an array consisting of only 0s, 1s, and 2s.

# Dutch National Flag Algorithm

class Solution(object):
    def sortColors(self,nums):
    # Three pointers
        low, mid, high = 0, 0, len(nums) - 1
    
    # Process until mid crosses high
        while mid <= high:
            if nums[mid] == 0:
            # Swap current element with low pointer
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
            # Leave 1 in the middle
                mid += 1
            else:  # nums[mid] == 2
            # Swap current element with high pointer
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
