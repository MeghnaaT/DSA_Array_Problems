# Find Pair with Given Sum: Find a pair of elements that adds up to a target sum.

def two_sum(self, arr, target):
    s = set()
    for num in arr:
        if target - num in s:
            return True
        s.add(num)
    return False

class Solution(object):
    def twoSum(self, nums, target):  #nums is the list(array) of integers
        #Dictionary to store number -> index
        seen={}  #-> empty hash map

        #Loop through the array nums
        for i, num in enumerate(nums): #enumerate(nums) gives both the index i and the value num at that index
            complement = target-num  #calculates the number we need to find to reach the target
            #if the complement already exists in dictionary,return indices
            if complement in seen:
                return [seen[complement],i]

            #otherwise, store the current number with its index
            seen[num]=i    
