class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        l=nums1[:m]
        l+=nums2[:n]
        l.sort()
        for i in range(len(l)):
            nums1[i] = l[i]