class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        n=len(nums)

        l=[]
        for num in range(2**n):
            s=[]
            for i in range(n):
                if (num & (1<<i)):
                    s.append(nums[i])
            l.append(s)
        return l



        