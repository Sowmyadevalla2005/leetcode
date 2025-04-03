class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        minn = float('inf')

        for n in nums:
            if n<minn:
                minn=n
        return minn




        