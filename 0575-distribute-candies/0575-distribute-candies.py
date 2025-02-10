class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        h={}
        c=0
        n=len(candyType)
        for i in candyType:
            h[i]=1
        for i in h:
            if c<n//2:
                c+=1
            else:
                break
        return c