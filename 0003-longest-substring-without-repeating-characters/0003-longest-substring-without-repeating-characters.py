class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        temp=''
        ans=0
        for i in range(n):
            while s[i] in temp:
                temp=temp[1:]
            temp+=s[i]
            ans=max(ans,len(temp))
        return ans