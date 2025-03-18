class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n=len(nums)
        res,sol = [],[]

        def backtrack(i):
            if i==n:
                res.append(sol[:])
                return 
            
            #pick a nums[i]

            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

            #dont pick nums[i]

            backtrack(i+1)

        backtrack(0)

        return res
