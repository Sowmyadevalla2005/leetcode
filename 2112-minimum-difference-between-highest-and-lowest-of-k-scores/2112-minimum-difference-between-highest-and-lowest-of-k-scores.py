class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans=float("inf")
        l=0
        n=len(nums)
        for r in range(n):
            if(r-l == k):
                l=l+1
            
            if(r-l==k-1):
                ans=min(ans,nums[r]-nums[l])
        return ans