# Find Intersection of Two Arrays: Find the common elements between two arrays.

class Solution(object):
    def intersection(self, nums1, nums2):
        set1 , set2= set(nums1), set(nums2)
        res = list(set1 & set2)
        
        return res            

