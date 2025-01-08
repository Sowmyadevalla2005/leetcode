class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count=0
        s={}
        for i in nums:
            if i not in s:
                s[i]=1
            else:
                s[i]+=1
        for k in s:
            if s[k]==1:
                return k
                

        