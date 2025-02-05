class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1==s2:
            return True
        
        s=[]
        for i , val in enumerate(s1):
            if val!=s2[i]:
                s.append(i)
        
        if len(s)!=2:
            return False
        k,m=s
        return s1[k]==s2[m] and s2[k]==s1[m]
            
        