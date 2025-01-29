class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        s={}
        cnt=0
        for num in nums:
            if num in s:
                s[num]+=1
            else:
                s[num]=1
        
        for k,v in s.items():
            if v==1:
                cnt+=k
        return cnt

        