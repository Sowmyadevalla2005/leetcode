class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:

        s=[]
        for i in nums:
            for j in range(i[0],i[1]+1):
                s.append(j)
        return len(set(s))
                
            
        