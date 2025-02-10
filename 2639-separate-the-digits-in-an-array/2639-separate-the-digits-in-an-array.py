class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[]
        for i in nums:
            s=str(i)
            for n in s:
                l.append(int(n))
        return l
            
        