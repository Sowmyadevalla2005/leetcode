class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_i=int(a,2)
        b_i=int(b,2)
        sum=a_i+b_i
        return bin(sum)[2:]
        