class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if not  s:
            return True
        c=0
        for i in t:
            if s[c]==i:
                c+=1
                if c==len(s):
                    return True
        return False
        