class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:

        n=len(nums)
        l=0
        r=0
        maxi=0
        bit=0

        while r<n:
            while(bit & nums[r] )!=0:
                bit=bit-nums[l]
                l=l+1
            
            bit= bit+nums[r]
            maxi=max(maxi,r-l+1)
            r+=1
            

        return maxi        