import heapq
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=sorted(list(set(nums)))
        if len(nums)>2:
            return nums[-3]
        else:
            return nums[-1]
        