# Merge Two Sorted Arrays

# 3 pointer method

class Solution:
    def merge(self, nums1, m, nums2, n):
        p1, p2, p = m - 1, n - 1, m + n - 1
        # p1 : last valid element in nums1
        # p2: last valid element in nums2
        # p: last position in nums1(where merged result goes)
        
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # If nums2 still has elements left
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
# TC: O(m+n)
# SC:O(1)
