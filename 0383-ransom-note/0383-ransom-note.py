class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        s={}

        for d in magazine:
            if d in s:
                s[d]+=1
            else:
                s[d]=1
        
        for i in ransomNote:
            if i in s and s[i]>0:
                s[i]-=1
            else:
                return False
        return True

        

        