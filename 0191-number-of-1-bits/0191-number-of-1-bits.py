class Solution:
    def hammingWeight(self, n: int) -> int:
        s=bin(n)
        w=s[1:]
        count=0
        for i in w:
            if i=='1':
                count+=1
        return count