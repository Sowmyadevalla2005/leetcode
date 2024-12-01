class Solution:
    def longestOnes(self, nums: List[int],  k: int) -> int:
        n=len(nums)
        l=0
        ans=0
        temp=0
        for r in range(n):
            if(nums[r]==0):
                temp=temp+1
    
            while(temp> k):
                if(nums[l]==0):
                    temp=temp-1
            
                l=l+1
            ans=max(ans,r-l+1)
        return ans