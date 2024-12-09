class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n=len(citations)
        freq=[0]*(n+1)
        for c in citations:
            if c>=n:
                freq[n]+=1
            else:
                freq[c]+=1
        
        idx=n
        count=freq[n]
        while count<idx:
            idx-=1
            count=count+freq[idx]
        return idx
        