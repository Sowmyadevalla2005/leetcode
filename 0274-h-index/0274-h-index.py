class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        l=len(citations)
        s=[0]*(l+1)
        for c in citations:
            s[min(l,c)]+=1
        
        h=l
        papers = s[h]
        while papers<h:
            h-=1
            papers+=s[h]
        return h
        
        