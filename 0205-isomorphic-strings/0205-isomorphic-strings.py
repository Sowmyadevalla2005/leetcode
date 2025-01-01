class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        l=[]
        m=[]
        for i in s:
            l.append(s.index(i))
        for i in t:
            m.append(t.index(i))

        if(l==m):
            return True
        else:
            return False