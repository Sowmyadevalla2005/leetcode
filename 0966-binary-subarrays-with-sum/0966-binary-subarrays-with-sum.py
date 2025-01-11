class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        
        def f(s):
            sm=count=left=0

            for right in range(len(nums)):
                sm+=nums[right]
                while left<=right and sm>s:
                    sm-=nums[left]
                    left+=1
                count+=(right-left+1)

            return count

        return f(goal)-f(goal-1)