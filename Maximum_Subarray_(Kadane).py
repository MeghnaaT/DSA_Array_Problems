# Maximum Sum Subarray (Kadane's Algorithm)

class Solution:
    def maxSubArray(self, nums):
        # Initialize with the first element
        max_sum = nums[0]
        current_sum = nums[0]
        
        # Traverse the array starting from the second element
        for i in range(1, len(nums)):
            # Either extend the current subarray or start a new one
            current_sum = max(nums[i], current_sum + nums[i])
            
            # Update the global maximum
            max_sum = max(max_sum, current_sum)
        
        return max_sum

# TC: O(n)
# SC: O(1)
