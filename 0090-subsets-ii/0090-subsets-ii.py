class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        n=len(nums) 
        s=set()

        for num in range(2**n):
            l=[]
            for i in range(n):
                if (num & (1<<i)):
                    l.append(nums[i])
            s.add(tuple(sorted(l)))

        return [list(x) for x in s]
        