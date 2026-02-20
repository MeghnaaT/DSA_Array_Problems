# Product of Array Except Self

class Solution(object):
    def productExceptSelf(self, nums):
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix #stores the product of all elements left of index i into res[i].
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1): # iterates from right to left over indices n-1 down to zero
            res[i] *= postfix
            postfix *= nums[i] # next elements has the product of all elements to the right of the next index to the left
        return res