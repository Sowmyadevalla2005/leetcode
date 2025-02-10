class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        s=set(candyType)
        t=len(candyType)//2
        return min(len(s),t)
        