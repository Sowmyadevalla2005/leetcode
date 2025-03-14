class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """

        t=sum(candies)
        if t<k:
            return 0
        
        l,r=1,t//k

        while(l<r):
            mid=(l+r+1)//2

            count = sum(candy//mid for candy in candies)

            if count>=k:
                l = mid

            else:
                r = mid-1
        
        return l



        