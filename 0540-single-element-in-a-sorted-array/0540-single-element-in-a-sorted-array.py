class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h={}
        for i in nums:
            if i not in h:
                h[i]=1
            else:
                h[i]+=1
        for k,v in h.items():
            if v==1:
                return k