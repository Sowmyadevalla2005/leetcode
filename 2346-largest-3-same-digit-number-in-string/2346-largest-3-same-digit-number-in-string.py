class Solution:
    def largestGoodInteger(self, num: str) -> str:
        l=""
        for i in range(len(num)-2):
            if num[i]==num[i+1]==num[i+2]:
                s=num[i:i+3]
                if l=="" or s>l:
                    l=s
        return l


        