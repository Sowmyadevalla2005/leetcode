class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        f={}

        for num in nums:
            if num in f:
                f[num]+=1
            else:
                f[num]=1

        even = all(c%2==0 for c in f.values())
        return even     