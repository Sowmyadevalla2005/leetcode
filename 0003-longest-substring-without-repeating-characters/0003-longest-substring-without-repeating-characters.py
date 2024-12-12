class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        n=len(s)
        temp=''
        ans=0
        for r in range(n):
            if s[r] not in temp:
                temp=temp+s[r]
            else:
                while s[r] in temp:
                    temp=temp[1:]
                    l=l+1
                temp=temp+s[r]
            ans=max(ans,r-l+1)
        return ans