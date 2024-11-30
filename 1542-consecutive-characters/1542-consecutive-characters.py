class Solution:
    def maxPower(self, s: str) -> int:
        maxx=1
        count=1
        n = len(s)
        for i in range(1,n):
            if(s[i]==s[i-1]):
                count=count+1
            else:
                count=1
            if(count>maxx):
                maxx=count
        return maxx
