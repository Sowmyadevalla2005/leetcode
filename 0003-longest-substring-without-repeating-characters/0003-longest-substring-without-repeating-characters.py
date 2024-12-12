class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        n=len(s)
        temp=[]
        ans=0
        for r in range(n):
            if s[r] not in temp:
                temp.append(s[r])
            else:
                while s[r] in temp:
                    temp.pop(0)
                    l=l+1
                temp.append(s[r])
            ans=max(ans,r-l+1)
        return ans