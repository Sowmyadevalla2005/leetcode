class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:

        t=sum(candies)
        if t<k:
            return 0

        l=1
        r=t//k

        while(l<r):
            mid = (l+r+1)//2

            count=sum(candy//mid for candy in candies)

            if count>=k:
                l = mid
            else:
                r=mid-1

        return l        