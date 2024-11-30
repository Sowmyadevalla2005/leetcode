class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxx=0
        count=0
        n=len(nums)
        for r in range(n):
            if(nums[r]==1):
                count=count+1
            else:
                count =0
            if(count>maxx):
                maxx=count
        return maxx


        