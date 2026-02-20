# Find the Longest Consecutive Sequence: Find the length of the longest consecutive sequence of integers.

class Solution(object):
    def longestConsecutive(self, nums):
        numSet = set(nums) # convert list into a hash set
        longest = 0 # track length of longest consecutive sequence

        for n in numSet:   # iterate over the set
            if (n - 1) not in numSet:  # if true, num is the start of sequence
                length = 1
                while (n + length) in numSet: # checks the current number
                    length += 1 # as length inc. check more consecutive numbers
                longest = max(longest, length)

        return longest



