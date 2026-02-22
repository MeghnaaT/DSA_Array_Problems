# Find Majority Element: Find the element that appears more than n/2 times.

# Boyer - Moore Voting Algorithm

class Solution:
    def majorityElement(self, nums):
        # Initialize candidate and counter
        candidate = None
        count = 0
        
        # Voting process
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        # Since the problem guarantees majority element exists,
        # candidate will be the answer
        return candidate
