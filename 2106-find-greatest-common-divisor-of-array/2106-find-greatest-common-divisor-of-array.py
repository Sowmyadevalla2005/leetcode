class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        a=min(nums)
        b=max(nums)
        def gcd(a,b):
            while b!=0:
                temp=b
                b=a%b
                a=temp
            return a

        return gcd(a,b)
        