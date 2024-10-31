class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d=-1
        m=-1
        dup=set()
        for i in range(len(nums)):
            v=nums[i]
            if v not in dup:
                dup.add(v)
            else:
                d=v
        for i in range(1,len(nums)+1):
            if i not in dup:
                m=i
        return (d,m)
                