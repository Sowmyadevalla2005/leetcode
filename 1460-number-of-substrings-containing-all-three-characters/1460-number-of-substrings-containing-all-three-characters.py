from collections import Counter
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l=0
        count=0
        c=Counter()

        for r in range(len(s)):
            if s[r] in "abc":
                c[s[r]]+=1 
            
            while c['a']>0 and c['b']>0 and c['c']>0:
                count+=len(s)-r
                c[s[l]]-=1
                l+=1
        return count


        