class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        summ=(0,0)
        for n in nums:
            summ=(summ[1],max(summ[0]+n,summ[1]))

        return summ[1]

        