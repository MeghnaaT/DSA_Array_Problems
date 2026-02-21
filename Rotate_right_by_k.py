# Rotate Array by k Positions: Rotate the array to the right by k positions.

# In-Place Reversal Method

class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k %=n
        
        def reverse(start,end):
            while start<end:
                nums[start], nums[end] = nums[end], nums[start]
                start +=1
                end -=1
        reverse(0, n-1) # reverse all
        reverse(0, k-1) # reverses first k elements of the now reversed array
        reverse(k, n-1) # reverses the remaining n-k elememts(from index k to end)
        
#TC = O(n)
# SC = O(1)
# Example:
# Original:      [1,2,3,4,5,6,7]
# Step 1:        [7,6,5,4,3,2,1]   (reverse all)
# Step 2:        [5,6,7,4,3,2,1]   (reverse first k)
# Step 3:        [5,6,7,1,2,3,4]   (reverse rest)
