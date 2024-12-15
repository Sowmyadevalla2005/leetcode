class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans=float("inf")
        l=0
        temp=0
        n=len(nums)

        if target in nums:
            return 1
        else:
            for r in range(n):
                temp+=nums[r]

                while temp>=target:
                    ans=min(ans,r-l+1)
                    temp-=nums[l]
                    l+=1

            if ans==float("inf"):
                return 0
            return ans
        
        