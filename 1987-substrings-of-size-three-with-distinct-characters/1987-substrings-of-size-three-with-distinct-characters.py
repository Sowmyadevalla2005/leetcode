class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n=len(s)
        l=0
        li=[]
        k=3
        c=0


        for r in range(n):
            li.append(s[r])
    
            if r-l==k:
                li.pop(0)
                l=l+1
            if(r-l==k-1):
                if len(set(li))==k:
                    c=c+1
        return c
      