class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        a=1
        j=0
        d=0

        for i in range(1,n):
            if nums[i]>=nums[i-1]:
                d=i
            if nums[i]<=nums[i-1]:
                j=i
            a=max(a,i-j+1,i-d+1)
        return a