class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=[-1,-1]
        if target not in nums:
            return l
        for i in range(len(nums)):
            if nums[i]==target:
                if l[0]==-1:
                    l[0]=i
                l[1]=i
        return l
